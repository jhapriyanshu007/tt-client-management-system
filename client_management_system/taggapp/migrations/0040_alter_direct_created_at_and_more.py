# Generated by Django 4.1.3 on 2022-12-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggapp', '0039_alter_direct_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='local_direct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
