# Generated by Django 5.0.6 on 2024-09-03 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0065_alter_course_semester_alter_resourcesbook_semester_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty'),
        ),
    ]
