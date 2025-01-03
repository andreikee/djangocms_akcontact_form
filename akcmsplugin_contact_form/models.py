from cms.models import CMSPlugin
from django.db import models


class ContactFormCMS(CMSPlugin):
    email = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )

    def __str__(self):
        return self.email


class ContactFormBaseFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_id = models.CharField(
        blank=False,
        max_length=50,
    )
    html_name = models.CharField(
        blank=False,
        max_length=50,
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )

    def __str__(self):
        return self.label


class ContactFormTextFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


class ContactFormEmailFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


class ContactFormPhoneFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    phone_pattern = models.CharField(
        blank=True,
        max_length=255
    )
    phone_max_length = models.CharField(
        blank=True,
        max_length=4
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


class ContactFormTextAreaFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    html_rows = models.CharField(
        blank=True,
        max_length=4
    )
    html_cols = models.CharField(
        blank=True,
        max_length=4
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


class ContactFormCheckboxFieldCMS(ContactFormBaseFieldCMS):
    value = models.CharField(
        blank=False,
        max_length=255
    )
    checked = models.BooleanField()


class ContactFormSubmitFieldCMS(ContactFormBaseFieldCMS):
    type = models.CharField(
        blank=False,
        max_length=255,
        choices=[
            ('button', 'Button'),
            ('input', 'Input')
        ]
    )
