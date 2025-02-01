from cms.models import CMSPlugin
from django.conf import settings
from django.db import models


class ContactFormCMS(CMSPlugin):
    email = models.CharField(
        default=settings.SITE_FROM_FORM_EMAIL,
        verbose_name="From Email",
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
    topic = models.CharField(
        blank=True,
        max_length=255
    )

    def __str__(self):
        return self.email


# class ContactFormBaseFieldCMS(CMSPlugin):
#     label = models.CharField(
#         blank=False,
#         max_length=255
#     )
#     html_classes = models.CharField(
#         blank=True,
#         max_length=255
#     )

#     def __str__(self):
#         return self.label


class ContactFormTextFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()

    def __str__(self):
        return self.label


class ContactFormEmailFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()

    def __str__(self):
        return self.label


class ContactFormPhoneFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
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

    def __str__(self):
        return self.label


class ContactFormTextAreaFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
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

    def __str__(self):
        return self.label


class ContactFormCheckboxFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
    value = models.CharField(
        blank=True,
        max_length=255
    )
    checked = models.BooleanField(blank=True)

    def __str__(self):
        return self.label


class ContactFormSubmitFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )
    type = models.CharField(
        blank=False,
        max_length=255,
        choices=[
            ('button', 'Button'),
            ('input', 'Input')
        ]
    )

    def __str__(self):
        return self.label
