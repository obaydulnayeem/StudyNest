# Generated by Django 5.0.6 on 2024-09-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0052_eduuniversity_discipline_batch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='moderator_type',
            field=models.CharField(blank=True, choices=[('Batch Moderator', 'Batch Moderator'), ('Departmental Moderator', 'Departmental Moderator'), ('Discipline Moderator', 'Discipline Moderator'), ('Institute Moderator', 'Institute Moderator'), ('University Moderator', 'University Moderator'), ('Central Moderator', 'Central Moderator')], max_length=100, null=True),
        ),
    ]
