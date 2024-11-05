# Generated by Django 5.0.6 on 2024-08-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_profile_email_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Guardian', 'Guardian'), ('Graduated', 'Graduated'), ('Govt. Employee', 'Govt. Employee'), ('Corporate/Company/Industry Employee', 'Corporate/Company/Industry Employee'), ('Visitor', 'Visitor'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
