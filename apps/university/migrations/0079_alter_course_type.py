# Generated by Django 5.0.6 on 2024-09-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0078_alter_course_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(blank=True, choices=[('Theory', 'Theory'), ('Laboratory', 'Laboratory'), ('Sessional', 'Sessional')], default='Theory', max_length=100, null=True),
        ),
    ]
