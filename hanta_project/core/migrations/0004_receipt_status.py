# Generated by Django 5.0.6 on 2024-06-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_receipt_receiptdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
