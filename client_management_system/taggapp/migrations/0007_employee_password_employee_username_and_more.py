# Generated by Django 4.1.3 on 2022-12-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0006_employee_first_name_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]
