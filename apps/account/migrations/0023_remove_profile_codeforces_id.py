# Generated by Django 5.0.6 on 2024-08-14 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_remove_profile_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='codeforces_id',
        ),
    ]
