# Generated by Django 5.0.6 on 2024-10-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_tracking', '0005_savedjobs_deadline_savedjobs_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='is_in_task',
            field=models.BooleanField(default=False),
        ),
    ]
