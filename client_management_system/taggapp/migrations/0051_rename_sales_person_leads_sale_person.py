# Generated by Django 4.1.3 on 2023-01-13 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0050_rename_lead_source_leads_sales_person_leads_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='sales_person',
            new_name='sale_person',
        ),
    ]
