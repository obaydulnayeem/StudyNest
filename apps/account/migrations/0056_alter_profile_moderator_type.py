# Generated by Django 5.0.6 on 2024-09-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0055_profile_given_prev_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='moderator_type',
            field=models.CharField(blank=True, choices=[('Batch Moderator', 'Batch Moderator'), ('Departmental Moderator', 'Departmental Moderator'), ('Discipline Moderator', 'Discipline Moderator'), ('Institute Moderator', 'Institute Moderator'), ('University Moderator', 'University Moderator')], max_length=100, null=True),
        ),
    ]
