# Generated by Django 5.0.6 on 2024-10-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_tracking', '0009_companylist_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=255)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
