# Generated by Django 4.2.3 on 2023-07-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_customuser_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
    ]