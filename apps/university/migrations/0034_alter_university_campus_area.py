# Generated by Django 5.0.6 on 2024-07-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0033_university_campus_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='campus_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
