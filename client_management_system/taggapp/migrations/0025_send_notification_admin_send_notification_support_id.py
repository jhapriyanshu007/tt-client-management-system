# Generated by Django 4.1.3 on 2022-12-16 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0024_send_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='send_notification',
            name='admin',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='send_notification',
            name='support_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taggapp.support'),
        ),
    ]
