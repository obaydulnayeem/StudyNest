# Generated by Django 5.0.6 on 2024-08-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_alter_eduuniversity_semester'),
        ('university', '0046_department_course_has_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='departments', to='account.profile'),
        ),
    ]
