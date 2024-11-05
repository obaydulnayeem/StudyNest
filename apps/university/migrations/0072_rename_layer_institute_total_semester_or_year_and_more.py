# Generated by Django 5.0.6 on 2024-09-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0071_alter_resourcesbook_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institute',
            old_name='layer',
            new_name='total_semester_or_year',
        ),
        migrations.AddField(
            model_name='institute',
            name='course_has_code',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='course_has_credit',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='course_has_hour',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='established',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='system',
            field=models.CharField(choices=[('Year', 'Year'), ('Semester', 'Semester')], default='Semester', max_length=100),
        ),
    ]