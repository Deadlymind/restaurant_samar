# Generated by Django 4.2.11 on 2024-04-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
