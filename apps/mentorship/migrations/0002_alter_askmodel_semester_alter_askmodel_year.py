# Generated by Django 5.0.6 on 2024-07-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askmodel',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='askmodel',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
    ]
