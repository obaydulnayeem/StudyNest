# Generated by Django 5.0.6 on 2024-07-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0025_alter_course_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='hour',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
