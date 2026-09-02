# akcmsplugin-contact-form

forked from [juliarizza/djangocms_contact_form](https://github.com/juliarizza/djangocms_contact_form)

Django-CMS contact form plugin with default Django email integration

## Available Fields

The following HTML fields can be added to the form:

- Text
- Email
- Phone
- Date, Time and Datetime
- Checkbox
- Radio
- Text Area
- Submit

## Installation

Install package:

```console
python -m pip install .
```

Add app to `settings.py`:

```python
INSTALLED_APPS = (
    ...
    'akcmsplugin_contact_form',
    ...
    )
```

Run migration:

```console
python manage.py migrate akcmsplugin_contact_form
```

## Upstream and Compatibility

This project is a maintained fork of
[juliarizza/djangocms_contact_form](https://github.com/juliarizza/djangocms_contact_form).
The fork exists to provide explicit packaging and compatibility metadata for
the Django CMS stack used by the consuming application, as well as application-
specific model and email-flow changes.

The upstream comparison and test evidence are documented in
[docs/UPSTREAM_COMPATIBILITY.md](docs/UPSTREAM_COMPATIBILITY.md). The current
fork declares support for Python 3.11-3.12, Django 5.1.x, and django CMS 4.1.x.

## Repository Maintenance

The default `master` branch should be changed through pull requests rather than
direct pushes. Recommended branch protection settings are documented in
[docs/REPOSITORY_MAINTENANCE.md](docs/REPOSITORY_MAINTENANCE.md).
