# Generated by Django 5.0.6 on 2024-07-30 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0031_rename_location_university_location_campus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='location_campus',
            new_name='location_permanent_campus',
        ),
    ]
