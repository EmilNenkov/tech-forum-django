# Generated by Django 3.2.3 on 2023-08-10 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_remove_customuser_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='slug',
        ),
    ]
