# Generated by Django 5.0.6 on 2024-10-05 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0058_alter_profile_moderator_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_type', models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Internship', 'Internship'), ('Contract', 'Contract'), ('Freelance', 'Freelance')], max_length=255, null=True)),
                ('work_environment', models.CharField(blank=True, choices=[('On-site', 'On-site'), ('Remote', 'Remote'), ('Hybrid', 'Hybrid')], max_length=255, null=True)),
                ('experience_level', models.CharField(blank=True, choices=[('Fresher', 'Fresher'), ('Mid-Senior', 'Mid-Senior'), ('Senior', 'Senior')], max_length=255, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('company_linkedin_link', models.URLField(blank=True, null=True)),
                ('company_location', models.CharField(blank=True, max_length=255, null=True)),
                ('date_applied', models.DateField()),
                ('job_description', models.TextField(blank=True, null=True)),
                ('expected_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('job_link', models.URLField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='')),
                ('hr_profile_link', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('current_status', models.TextField(blank=True, null=True)),
                ('cause_of_cancellation', models.TextField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_applications_tracker', to='account.profile')),
            ],
        ),
    ]