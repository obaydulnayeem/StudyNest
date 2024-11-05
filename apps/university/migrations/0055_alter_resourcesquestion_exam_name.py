# Generated by Django 5.0.6 on 2024-08-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0054_department_established_department_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcesquestion',
            name='exam_name',
            field=models.CharField(choices=[('1st Mid', '1st Mid'), ('2nd Mid', '2nd Mid'), ('3rd Mid', '3rd Mid'), ('Class Test', 'Class Test'), ('Quiz', 'Quiz'), ('Supply', 'Supply'), ('Final', 'Final'), ('Lab Test', 'Lab Test'), ('Lab Final', 'Lab Final'), ('Others', 'Others')], max_length=50),
        ),
    ]
