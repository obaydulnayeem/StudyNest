# Generated by Django 5.0.6 on 2024-08-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0039_profile_referral_code_profile_referred_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referred_by_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]