from __future__ import annotations

import importlib
import importlib.util
import subprocess
import sys
import tarfile
import zipfile
from email.parser import Parser
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = PROJECT_ROOT / "akcmsplugin_contact_form"


def _source_package_files() -> set[str]:
    return {
        path.relative_to(PROJECT_ROOT).as_posix()
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix not in {".pyc", ".pyo"}
    }


def _wheel_members(path: Path) -> set[str]:
    with zipfile.ZipFile(path) as archive:
        return set(archive.namelist())


def _sdist_members(path: Path) -> set[str]:
    with tarfile.open(path, mode="r:gz") as archive:
        names = {member.name for member in archive.getmembers()}

    roots = {name.split("/", 1)[0] for name in names if name}
    assert len(roots) == 1
    root = next(iter(roots))
    return {
        name.removeprefix(f"{root}/")
        for name in names
        if name != root
    }


def _wheel_metadata(path: Path):
    with zipfile.ZipFile(path) as archive:
        metadata_name = next(
            name for name in archive.namelist()
            if name.endswith(".dist-info/METADATA")
        )
        return Parser().parsestr(archive.read(metadata_name).decode("utf-8"))


def _sdist_file(path: Path, relative_path: str) -> str:
    with tarfile.open(path, mode="r:gz") as archive:
        root = next(
            item.name.rstrip("/")
            for item in archive.getmembers()
            if item.name and "/" not in item.name.rstrip("/")
        )
        member = archive.getmember(f"{root}/{relative_path}")
        extracted = archive.extractfile(member)
        assert extracted is not None
        return extracted.read().decode("utf-8")


@pytest.fixture(scope="session")
def built_artifacts(
    tmp_path_factory: pytest.TempPathFactory,
) -> tuple[Path, Path]:
    if importlib.util.find_spec("build") is None:
        pytest.skip(
            "The optional build dependency is required for artifact checks"
        )

    output_dir = tmp_path_factory.mktemp("package-artifacts")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--no-isolation",
            "--wheel",
            "--sdist",
            "--outdir",
            str(output_dir),
            str(PROJECT_ROOT),
        ],
        cwd=PROJECT_ROOT,
        check=True,
    )

    wheel = next(output_dir.glob("*.whl"))
    sdist = next(output_dir.glob("*.tar.gz"))
    return wheel, sdist


def test_public_package_import_and_version() -> None:
    package = importlib.import_module("akcmsplugin_contact_form")
    assert package.__version__ == "0.3"


def test_django_app_config_and_migration_import() -> None:
    if importlib.util.find_spec("django") is None:
        pytest.skip("Django is required for the compatibility import check")

    app_config = importlib.import_module("akcmsplugin_contact_form.apps")
    migration = importlib.import_module(
        "akcmsplugin_contact_form.migrations.0001_initial"
    )

    assert app_config.CmspluginContactFormConfig.name == (
        "akcmsplugin_contact_form"
    )
    assert migration.Migration.initial is True


def test_distributions_include_all_package_files(built_artifacts) -> None:
    wheel, sdist = built_artifacts
    source_files = _source_package_files()

    wheel_members = _wheel_members(wheel)
    sdist_members = _sdist_members(sdist)

    assert source_files <= wheel_members
    assert source_files <= sdist_members

    for members in (wheel_members, sdist_members):
        assert not any(Path(name).is_absolute() for name in members)
        assert not any("__pycache__" in name for name in members)
        assert not any(name.endswith((".pyc", ".pyo")) for name in members)
        assert not any(
            part in {".env", ".git", "build", "dist", ".venv", "venv"}
            for name in members
            for part in name.split("/")
        )
        assert not any(
            Path(name).name in {"db.sqlite3", "local_settings.py"}
            for name in members
        )


def test_built_metadata_and_license(built_artifacts) -> None:
    wheel, sdist = built_artifacts
    license_text = (PROJECT_ROOT / "LICENSE").read_text(encoding="utf-8")
    metadata_documents = (
        _wheel_metadata(wheel),
        Parser().parsestr(_sdist_file(sdist, "PKG-INFO")),
    )

    for metadata in metadata_documents:
        assert metadata["Name"] == "akcmsplugin-contact-form"
        assert metadata["Version"] == "0.3"
        assert metadata["Requires-Python"] == "<3.12,>=3.11"
        assert metadata["License-Expression"] == "MIT"
        assert metadata.get_all("License-File") == ["LICENSE"]
        requirements = {
            requirement.replace(" ", "")
            for requirement in metadata.get_all("Requires-Dist")
        }
        assert "Django<5.2,>=5.1.3" in requirements
        assert "django-cms<4.2,>=4.1.4" in requirements
        assert "build<2,>=1.2;extra==\"test\"" in requirements
        assert "packaging>=24.2;extra==\"test\"" in requirements
        assert "pytest<9,>=7.4;extra==\"test\"" in requirements
        assert "setuptools>=77;extra==\"test\"" in requirements
        assert "wheel>=0.43;extra==\"test\"" in requirements

    with zipfile.ZipFile(wheel) as archive:
        license_name = next(
            name for name in archive.namelist()
            if ".dist-info/" in name and name.endswith("/LICENSE")
        )
        assert archive.read(license_name).decode("utf-8") == license_text

    assert _sdist_file(sdist, "LICENSE") == license_text
    assert "Copyright (c) 2020 Júlia Rizza" in license_text
    assert "Copyright (c) 2020 Andrei Krivoshei" in license_text
