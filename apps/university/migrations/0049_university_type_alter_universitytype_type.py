# Generated by Django 5.0.6 on 2024-08-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0048_alter_resourcesbook_uploaded_by_prev_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='type',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('Science and Technology', 'Science and Technology'), ('Engineering', 'Engineering')], default='Public', max_length=100),
        ),
        migrations.AlterField(
            model_name='universitytype',
            name='type',
            field=models.CharField(default='Public', max_length=100),
        ),
    ]
