# Generated by Django 5.0.6 on 2024-07-12 06:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_eduuniversity_department_eduuniversity_faculty_and_more'),
        ('university', '0006_delete_lecturemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcesQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')], max_length=5, null=True)),
                ('semester', models.PositiveIntegerField(blank=True, choices=[(1, '1st Semester'), (2, '2nd Semester'), (3, '3rd Semester'), (4, '4th Semester'), (5, '5th Semester'), (6, '6th Semester'), (7, '7th Semester'), (8, '8th Semester')], null=True)),
                ('exam_name', models.CharField(choices=[('1st Mid', '1st Mid'), ('2nd Mid', '2nd Mid'), ('3rd Mid', '3rd Mid'), ('Class Test', 'Class Test'), ('Lab Test', 'Lab Test'), ('Lab Final', 'Lab Final'), ('Final', 'Final')], max_length=50)),
                ('session', models.CharField(choices=[('24-25', '24-25'), ('23-24', '23-24'), ('22-23', '22-23'), ('21-22', '21-22'), ('20-21', '20-21'), ('19-20', '19-20'), ('18-19', '18-19')], max_length=9)),
                ('question_file', models.FileField(upload_to='study/questions/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.department')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.university')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]