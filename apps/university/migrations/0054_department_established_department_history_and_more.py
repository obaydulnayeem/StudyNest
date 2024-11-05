# Generated by Django 5.0.6 on 2024-08-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0008_moderatorrequest_is_running'),
        ('university', '0053_department_moderators'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='established',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='universities', to='admin_panel.moderatorrequest'),
        ),
    ]