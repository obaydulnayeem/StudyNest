# Generated by Django 5.0.6 on 2024-09-06 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0070_course_status_course_type_alter_department_system_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcesbook',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AlterField(
            model_name='resourceslecture',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AlterField(
            model_name='resourcesnote',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AlterField(
            model_name='resourcesquestion',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
    ]
