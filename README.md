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

```
pip install akcmsplugin-contact-form
```

Add app to `settings.py`:

```
INSTALLED_APPS = (
    ...
    'akcmsplugin_contact_form',
    ...
    )
```

Run migration:

```
python manage.py migrate akcmsplugin_contact_form
```
