# Generated by Django 5.0 on 2024-02-25 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_company_id_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='location',
        ),
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.AlterField(
            model_name='job_post',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company'),
        ),
    ]
