# Generated by Django 5.0.6 on 2024-10-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_tracking', '0011_followee_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='followee',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
