# Generated by Django 5.0.6 on 2024-08-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feedback',
            name='love_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]