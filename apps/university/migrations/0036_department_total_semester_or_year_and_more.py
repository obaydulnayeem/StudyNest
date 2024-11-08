# Generated by Django 5.0.6 on 2024-08-01 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0035_alter_resourcesbook_uploaded_by_prev_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='total_semester_or_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='system',
            field=models.CharField(choices=[('Year', 'Year'), ('Semester', 'Semester')], default='semester', max_length=100),
        ),
    ]
