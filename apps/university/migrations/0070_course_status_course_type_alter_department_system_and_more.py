# Generated by Django 5.0.6 on 2024-09-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0069_course_center_course_discipline_course_institute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('Mandatory', 'Mandatory'), ('Optional', 'Optional')], default='Mandatory', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('Theory', 'Theory'), ('Laboratory', 'Laboratory')], default='Theory', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='system',
            field=models.CharField(choices=[('Year', 'Year'), ('Semester', 'Semester')], default='Semester', max_length=100),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='system',
            field=models.CharField(choices=[('Year', 'Year'), ('Semester', 'Semester')], default='Semester', max_length=100),
        ),
    ]
