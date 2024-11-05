# Generated by Django 5.0.6 on 2024-08-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_alter_profile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='moderator_type',
            field=models.CharField(blank=True, choices=[('Batch Moderator', 'Batch Moderator'), ('Departmental Moderator', 'Departmental Moderator'), ('University Moderator', 'University Moderator'), ('Central Moderator', 'Central Moderator')], max_length=100, null=True),
        ),
    ]