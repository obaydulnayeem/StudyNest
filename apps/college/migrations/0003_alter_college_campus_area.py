# Generated by Django 5.0.6 on 2024-08-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_rename_motto_college_former_name_college_acronym_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='campus_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
