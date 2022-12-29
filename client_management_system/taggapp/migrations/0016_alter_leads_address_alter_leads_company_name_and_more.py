# Generated by Django 4.1.3 on 2022-12-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0015_alter_leads_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='contact_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='contact_person',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='email_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='feedback',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='lead_source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='product',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
