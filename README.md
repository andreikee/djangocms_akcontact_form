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
