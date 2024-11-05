# Generated by Django 5.0.6 on 2024-09-05 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0068_remove_university_layer1_remove_university_layer1_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.center'),
        ),
        migrations.AddField(
            model_name='course',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.discipline'),
        ),
        migrations.AddField(
            model_name='course',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.institute'),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.school'),
        ),
        migrations.AddField(
            model_name='resourcesbook',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.center'),
        ),
        migrations.AddField(
            model_name='resourcesbook',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.discipline'),
        ),
        migrations.AddField(
            model_name='resourcesbook',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.institute'),
        ),
        migrations.AddField(
            model_name='resourcesbook',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.school'),
        ),
        migrations.AddField(
            model_name='resourceslecture',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.center'),
        ),
        migrations.AddField(
            model_name='resourceslecture',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.discipline'),
        ),
        migrations.AddField(
            model_name='resourceslecture',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.institute'),
        ),
        migrations.AddField(
            model_name='resourceslecture',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.school'),
        ),
        migrations.AddField(
            model_name='resourcesnote',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.center'),
        ),
        migrations.AddField(
            model_name='resourcesnote',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.discipline'),
        ),
        migrations.AddField(
            model_name='resourcesnote',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.institute'),
        ),
        migrations.AddField(
            model_name='resourcesnote',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.school'),
        ),
        migrations.AddField(
            model_name='resourcesquestion',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.center'),
        ),
        migrations.AddField(
            model_name='resourcesquestion',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.discipline'),
        ),
        migrations.AddField(
            model_name='resourcesquestion',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.institute'),
        ),
        migrations.AddField(
            model_name='resourcesquestion',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.school'),
        ),
    ]
