# Generated by Django 5.0.6 on 2024-07-12 05:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_eduuniversity_department_eduuniversity_faculty_and_more'),
        ('university', '0004_resourcesbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcesLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')], max_length=5, null=True)),
                ('semester', models.PositiveIntegerField(blank=True, choices=[(1, '1st Semester'), (2, '2nd Semester'), (3, '3rd Semester'), (4, '4th Semester'), (5, '5th Semester'), (6, '6th Semester'), (7, '7th Semester'), (8, '8th Semester')], null=True)),
                ('session', models.CharField(choices=[('24-25', '24-25'), ('23-24', '23-24'), ('22-23', '22-23'), ('21-22', '21-22'), ('20-21', '20-21'), ('19-20', '19-20'), ('18-19', '18-19')], max_length=50)),
                ('lecture_title', models.CharField(max_length=200)),
                ('lecture_author', models.CharField(max_length=100)),
                ('lecture_file', models.FileField(upload_to='study/lectures/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.department')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.university')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='BookModel',
        ),
    ]