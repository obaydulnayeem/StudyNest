# Generated by Django 5.0.6 on 2024-09-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0082_department_syllabus_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commoncourse',
            name='type',
        ),
        migrations.AddField(
            model_name='commoncourse',
            name='course_type',
            field=models.CharField(blank=True, choices=[('Theory', 'Theory'), ('Laboratory/Practical', 'Laboratory/Practical'), ('Sessional', 'Sessional'), ('Thesis/Project', 'Thesis/Project')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='commoncourse',
            name='motivation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoncourse',
            name='objectives',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoncourse',
            name='outcomes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoncourse',
            name='prerequisite',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commoncourse',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
    ]
