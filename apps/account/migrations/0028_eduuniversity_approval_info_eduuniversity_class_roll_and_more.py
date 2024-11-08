# Generated by Django 5.0.6 on 2024-08-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_profile_facebook_id_visibility_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduuniversity',
            name='approval_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eduuniversity',
            name='class_roll',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eduuniversity',
            name='degree',
            field=models.CharField(blank=True, choices=[('Bachelor of Science (B.Sc)', 'Bachelor of Science (B.Sc)'), ('Bachelor of Arts (B.A)', 'Bachelor of Arts (B.A)'), ('Bachelor of Business Administration (BBA)', 'Bachelor of Business Administration (BBA)'), ('Bachelor of Business Studies (BBS)', 'Bachelor of Business Studies (BBS)'), ('Bachelor of Commerce (B.Com)', 'Bachelor of Commerce (B.Com)'), ('Bachelor of Law (B.L)', 'Bachelor of Law (B.L)'), ('Bachelor of Engineering (B.E)', 'Bachelor of Engineering (B.E)'), ('Bachelor of Technology (B.Tech)', 'Bachelor of Technology (B.Tech)'), ('Bachelor of Pharmacy (B.Pharm)', 'Bachelor of Pharmacy (B.Pharm)'), ('Bachelor of Architecture (B.Arch)', 'Bachelor of Architecture (B.Arch)'), ('Bachelor of Fine Arts (BFA)', 'Bachelor of Fine Arts (BFA)'), ('Bachelor of Social Science (BSS)', 'Bachelor of Social Science (BSS)'), ('Bachelor of Environmental Science (BES)', 'Bachelor of Environmental Science (BES)'), ('Bachelor of Veterinary Science (BVSc)', 'Bachelor of Vet Science (BVSc)'), ('Bachelor of Hotel Management (BHM)', 'Bachelor of Hotel Management (BHM)'), ('Bachelor of Music (BM)', 'Bachelor of Music (BM)'), ('Others', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
