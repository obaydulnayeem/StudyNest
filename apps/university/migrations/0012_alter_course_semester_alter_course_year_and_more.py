# Generated by Django 5.0.6 on 2024-07-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0011_alter_resourcesbook_book_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesbook',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesbook',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourceslecture',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourceslecture',
            name='session',
            field=models.CharField(choices=[('24-25', '24-25'), ('23-24', '23-24'), ('22-23', '22-23'), ('21-22', '21-22'), ('20-21', '20-21'), ('19-20', '19-20'), ('18-19', '18-19'), ('17-18', '17-18'), ('16-17', '16-17'), ('15-16', '15-16'), ('14-15', '14-15'), ('13-14', '13-14')], max_length=50),
        ),
        migrations.AlterField(
            model_name='resourceslecture',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesnote',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesnote',
            name='session',
            field=models.CharField(choices=[('24-25', '24-25'), ('23-24', '23-24'), ('22-23', '22-23'), ('21-22', '21-22'), ('20-21', '20-21'), ('19-20', '19-20'), ('18-19', '18-19'), ('17-18', '17-18'), ('16-17', '16-17'), ('15-16', '15-16'), ('14-15', '14-15'), ('13-14', '13-14')], max_length=50),
        ),
        migrations.AlterField(
            model_name='resourcesnote',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesquestion',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesquestion',
            name='session',
            field=models.CharField(choices=[('24-25', '24-25'), ('23-24', '23-24'), ('22-23', '22-23'), ('21-22', '21-22'), ('20-21', '20-21'), ('19-20', '19-20'), ('18-19', '18-19'), ('17-18', '17-18'), ('16-17', '16-17'), ('15-16', '15-16'), ('14-15', '14-15'), ('13-14', '13-14')], max_length=9),
        ),
        migrations.AlterField(
            model_name='resourcesquestion',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('Graduated', 'Graduated')], max_length=50, null=True),
        ),
    ]
