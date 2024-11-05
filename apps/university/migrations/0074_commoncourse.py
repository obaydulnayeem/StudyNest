# Generated by Django 5.0.6 on 2024-09-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0073_school_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Theory', 'Theory'), ('Laboratory', 'Laboratory')], default='Theory', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('syllabus', models.TextField(blank=True, null=True)),
            ],
        ),
    ]