# Generated by Django 5.1.6 on 2025-02-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bank_pin',
            field=models.IntegerField(default=0),
        ),
    ]
