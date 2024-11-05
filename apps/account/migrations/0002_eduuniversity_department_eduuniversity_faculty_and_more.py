# Generated by Django 5.0.6 on 2024-07-12 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduuniversity',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AddField(
            model_name='eduuniversity',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty'),
        ),
        migrations.AddField(
            model_name='eduuniversity',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.university'),
        ),
        migrations.AddField(
            model_name='eduuniversity',
            name='university_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.universitytype'),
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AddField(
            model_name='profile',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty'),
        ),
        migrations.AddField(
            model_name='profile',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.university'),
        ),
    ]
