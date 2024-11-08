# Generated by Django 5.0.6 on 2024-09-18 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0091_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcesquestion',
            name='exam_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourcesquestion',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.teacher'),
        ),
    ]
