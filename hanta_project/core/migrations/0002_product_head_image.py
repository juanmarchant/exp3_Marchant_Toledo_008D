# Generated by Django 5.0.6 on 2024-06-24 22:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.custom_upload_head_image),
        ),
    ]
