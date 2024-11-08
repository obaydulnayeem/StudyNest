# Generated by Django 5.0.6 on 2024-08-20 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_alter_profile_moderator_type'),
        ('admin_panel', '0007_moderatorrequest_approved_initial_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='moderator_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_moderator_info', to='admin_panel.moderatorrequest'),
        ),
    ]
