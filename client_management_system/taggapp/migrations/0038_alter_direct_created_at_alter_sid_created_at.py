# Generated by Django 4.1.3 on 2022-12-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0037_alter_local_direct_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sid',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]