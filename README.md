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

1. Copy the folder `akcmsplugin_contact_form` into the Django project root folder.

<!-- ```
pip install akcmsplugin-contact-form
``` -->

2. Add app to `settings.py`:

```
INSTALLED_APPS = (
    ...
    'akcmsplugin_contact_form',
    ...
    )
```

3. Run migration:

```
python manage.py migrate akcmsplugin_contact_form
```
