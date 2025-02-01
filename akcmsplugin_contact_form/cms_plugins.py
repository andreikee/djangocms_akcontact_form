from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from . import models


@plugin_pool.register_plugin
class ContactFormCMSPlugin(CMSPluginBase):
    model = models.ContactFormCMS
    name = _("Contact Form")
    render_template = "akcmsplugin_contact_form/form.html"
    allow_children = True
    child_classes = [
        "ContactFormTextFieldCMSPlugin",
        "ContactFormEmailFieldCMSPlugin",
        "ContactFormPhoneFieldCMSPlugin",
        "ContactFormTextAreaFieldCMSPlugin",
        "ContactFormCheckboxFieldCMSPlugin",
        "ContactFormRadioFieldCMSPlugin",
        "ContactFormDateFieldCMSPlugin",
        "ContactFormTimeFieldCMSPlugin",
        "ContactFormDateTimeFieldCMSPlugin",
        "ContactFormSubmitFieldCMSPlugin"
    ]

    def render(self, context, instance, placeholder):
        instance.is_success = False
        instance.success_message_title = _("Thank you for your message.")
        instance.success_message_body = _("We will get back to you soon.")

        context = super().render(context, instance, placeholder)

        request = context["request"]
        if request.method == "POST":

            subject = "LuckyKV - " + " " + _(instance.topic)

            message = subject + ":" + "\n\n"

            visitor_email_field = [  # noqa: RUF015
                inst for inst in instance.child_plugin_instances
                if isinstance(inst, models.ContactFormEmailFieldCMS)
            ][0]

            visitor_email_key = slugify(visitor_email_field.label)
            visitor_email = request.POST[visitor_email_key]

            # print("Topic:", instance.topic)
            # print("instance:", instance)
            # print("email_field:", email_field)
            # print("email_key:", email_key)
            # print("request.POST:", email)

            submit_field = [  # noqa: RUF015
                inst for inst in instance.child_plugin_instances
                if isinstance(inst, models.ContactFormSubmitFieldCMS)
            ][0]
            submit_key = slugify(submit_field.label)

            for key in request.POST:
                if key in ["csrfmiddlewaretoken", submit_key]:
                    continue

                message += f"{key.capitalize()}: {request.POST[key]}\n"

            EmailMessage(
                subject=subject,
                body=message,
                from_email=instance.email,
                to=[instance.email],
                # from_email=settings.SITE_FROM_FORM_EMAIL,
                # to=[settings.SITE_FROM_FORM_EMAIL],
                # reply_to=[instance.email],
                bcc=[visitor_email],
            ).send()

            instance.is_success = True

            # return HttpResponseRedirect("/thanks/")

        context.update({
            "placeholder": placeholder,
            "instance": instance
        })

        return context


@plugin_pool.register_plugin
class ContactFormTextFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = _("Text Field")
    render_template = "akcmsplugin_contact_form/text_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormEmailFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormEmailFieldCMS
    name = _("Email Field")
    render_template = "akcmsplugin_contact_form/email_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormPhoneFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormPhoneFieldCMS
    name = _("Phone Field")
    render_template = "akcmsplugin_contact_form/phone_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormTextAreaFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextAreaFieldCMS
    name = _("Text Area Field")
    render_template = "akcmsplugin_contact_form/textarea_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormCheckboxFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormCheckboxFieldCMS
    name = _("Checkbox Field")
    render_template = "akcmsplugin_contact_form/checkbox_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormRadioFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormCheckboxFieldCMS
    name = _("Radio Field")
    render_template = "akcmsplugin_contact_form/radio_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormDateFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = _("Date Field")
    render_template = "akcmsplugin_contact_form/date_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormTimeFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = _("Time Field")
    render_template = "akcmsplugin_contact_form/time_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormDateTimeFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = "Date & Time Field"
    render_template = "akcmsplugin_contact_form/datetime_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]


@plugin_pool.register_plugin
class ContactFormSubmitFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormSubmitFieldCMS
    name = _("Submit Field")
    render_template = "akcmsplugin_contact_form/submit_field.html"
    require_parent = True
    parent_classes = ["ContactFormCMSPlugin"]
