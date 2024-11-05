# Generated by Django 5.0.6 on 2024-09-18 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0094_alter_teacher_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, choices=[('Lecturer', 'Lecturer'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.discipline'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.institute'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.school'),
        ),
    ]