# Generated by Django 4.1.3 on 2022-12-05 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0008_remove_employee_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Employees',
        ),
    ]
