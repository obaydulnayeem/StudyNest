# Generated by Django 5.0.6 on 2024-07-15 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_pendingusermodel_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingusermodel',
            name='requested_profile',
        ),
    ]
