# Generated by Django 5.0.6 on 2024-08-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0042_university_colors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='motto',
            new_name='motto_bangla',
        ),
        migrations.AddField(
            model_name='university',
            name='acronym',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='former_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='motto_english',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]