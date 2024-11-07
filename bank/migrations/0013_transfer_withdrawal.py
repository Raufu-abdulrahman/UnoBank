# Generated by Django 4.2.4 on 2024-11-07 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0012_alter_deposit_amount_alter_deposit_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=8, verbose_name='Account Number')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('pin', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Amount')),
                ('pin', models.CharField(max_length=4)),
            ],
        ),
    ]