# Generated by Django 4.1.3 on 2022-12-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0023_remove_send_notification_hr_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='send_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]