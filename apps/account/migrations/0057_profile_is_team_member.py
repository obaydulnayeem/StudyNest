# Generated by Django 5.0.6 on 2024-09-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0056_alter_profile_moderator_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_team_member',
            field=models.BooleanField(default=False),
        ),
    ]