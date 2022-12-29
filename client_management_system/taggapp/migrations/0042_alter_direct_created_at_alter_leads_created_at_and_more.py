# Generated by Django 4.1.3 on 2022-12-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0041_alter_leads_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='local_direct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='sid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
