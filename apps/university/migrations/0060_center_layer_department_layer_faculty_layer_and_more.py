# Generated by Django 5.0.6 on 2024-08-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0059_university_has_center_university_has_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='layer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='layer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='layer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='layer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='layer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='layer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]