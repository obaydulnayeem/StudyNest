# Generated by Django 5.0.6 on 2024-08-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_eduuniversity_creation_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eduuniversity',
            old_name='creation_date',
            new_name='created_at',
        ),
    ]