# Generated by Django 4.2.11 on 2024-05-06 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_full_name_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
