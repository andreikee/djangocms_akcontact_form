# Upstream Compatibility

## Comparison Scope

This comparison was performed on 2026-09-02 using these public repository
snapshots:

- Upstream: `juliarizza/djangocms_contact_form`, `master`, commit
  `421408eb3ae6d0fed7d674400371663cb5338fa2`.
- Fork: `andreikee/djangocms_akcontact_form`, package `master`, merge commit
  `a5ea1c255d75168f8871dd9b97dbd9e932fad15e`.

The upstream repository is archived and exposes only its `master` branch. The
fork is active and keeps the upstream link for provenance.

## Upstream Findings

The upstream README documents installation and available fields, but does not
state supported Django or django CMS versions. Its legacy `setup.py` declares
only `setuptools` as an install requirement. The reviewed upstream snapshot has
no `pyproject.toml`, requirements file, CI workflow, or test suite.

The upstream package builds successfully on Python 3.12.14. Running its test
command reports `no tests ran`. A direct import check using Django 5.1.4 fails
because `cmsplugin_contact_form.models` imports
`django.utils.encoding.python_2_unicode_compatible`, which is unavailable in
Django 5.1.4. This is evidence about the reviewed upstream `master` snapshot;
it is not a claim about every historical upstream release.

The upstream package also uses the `cmsplugin_contact_form` module name and
does not declare a Django CMS version range. Its plugin code opens an SMTP
connection from model fields, so the consuming application must supply and
maintain that configuration itself.

## Fork Changes

The forked package changes are intentional and application-facing:

- The package and Django app namespace are `akcmsplugin_contact_form`.
- `pyproject.toml` declares Python `>=3.11,<3.13`, Django `>=5.1.3,<5.2`, and
  django CMS `>=4.1.4,<4.2`.
- The package metadata includes templates and translation files and uses a
  modern build configuration.
- The app configuration uses Django's `BigAutoField` default.
- The contact-form model adds a `topic` field and uses the application's
  configured Django email backend rather than storing SMTP credentials in the
  form model.
- The fork contains focused build, metadata, license, app, and migration
  checks.

## Qualification Evidence

The LKV-024 qualification was run in a fresh Python 3.12.14 environment. The
declared Django 5.1.x and django CMS 4.1.x compatibility line was installed;
the focused package suite reported `4 passed`, including wheel and source
distribution checks, metadata, license preservation, app configuration, and
migration import. `pip check` also passed.

These results support the declared version range and the tested package
snapshot. They do not replace application-level regression tests or imply
support for untested framework versions.

## Maintenance Policy

The fork should document intentional upstream divergence when behavior,
packaging, or compatibility changes. New upstream changes should be reviewed
against the application-specific model and email flow before being adopted.