# Generated by Django 5.1.6 on 2025-02-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('occupation', models.CharField(max_length=255)),
                ('dor', models.DateField(auto_now_add=True)),
                ('balance', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=255)),
                ('upi', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('users_name', models.CharField(max_length=255)),
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_amt', models.IntegerField()),
                ('credit_or_debit', models.CharField(max_length=30)),
                ('to_from_user', models.CharField(max_length=30)),
            ],
        ),
    ]
