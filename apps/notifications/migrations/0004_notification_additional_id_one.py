# Generated by Django 5.0.6 on 2024-08-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='additional_id_one',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
