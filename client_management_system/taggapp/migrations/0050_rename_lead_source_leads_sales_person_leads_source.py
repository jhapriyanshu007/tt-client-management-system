# Generated by Django 4.1.3 on 2023-01-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0049_clients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='lead_source',
            new_name='sales_person',
        ),
        migrations.AddField(
            model_name='leads',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
