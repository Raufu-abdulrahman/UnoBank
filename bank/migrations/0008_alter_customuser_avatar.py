# Generated by Django 4.2.4 on 2024-11-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.CharField(default='avatars/avatar1.jpg', max_length=100),
        ),
    ]