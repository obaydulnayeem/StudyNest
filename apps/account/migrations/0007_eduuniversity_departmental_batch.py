# Generated by Django 5.0.6 on 2024-07-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_eduuniversity_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduuniversity',
            name='departmental_batch',
            field=models.CharField(blank=True, choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], max_length=50, null=True),
        ),
    ]
