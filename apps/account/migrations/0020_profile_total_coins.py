# Generated by Django 5.0.6 on 2024-08-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_cointransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_coins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
