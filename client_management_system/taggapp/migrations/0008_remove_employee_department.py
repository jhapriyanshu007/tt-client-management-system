# Generated by Django 4.1.3 on 2022-12-05 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0007_employee_password_employee_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
    ]
