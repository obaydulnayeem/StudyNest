# Generated by Django 5.0.6 on 2024-08-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0043_alter_profile_email_visibility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Other', 'Other')], default='Student', max_length=100, null=True),
        ),
    ]