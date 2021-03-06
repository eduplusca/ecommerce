# Generated by Django 2.2.16 on 2020-11-02 07:04

from django.db import migrations, models
from oscar.core.loading import get_model

from ecommerce.extensions.offer.constants import NUDGE_EMAIL_TEMPLATES, TEMPLATES_NAME


CodeAssignmentNudgeEmailTemplates = get_model('offer', 'CodeAssignmentNudgeEmailTemplates')


def create_code_assignemnt_nudge_email_templates(apps, schema_editor):
    """Create nudge email templates."""
    for template in NUDGE_EMAIL_TEMPLATES:
        CodeAssignmentNudgeEmailTemplates.objects.create(**template)


def remove_code_assignemnt_nudge_email_templates(apps, schema_editor):
    """Remove nudge email templates."""
    CodeAssignmentNudgeEmailTemplates.objects.filter(name__in=TEMPLATES_NAME).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0046_offerassignmentemailsentrecord')
    ]
    operations = [
        migrations.RunPython(create_code_assignemnt_nudge_email_templates, remove_code_assignemnt_nudge_email_templates)
    ]
