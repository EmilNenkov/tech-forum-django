# Generated by Django 4.2.3 on 2023-07-26 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_customuser_date_created_alter_topic_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='John Smith', max_length=100, validators=[django.core.validators.MinLengthValidator(4, message='Full name must be at least 4 characters long.'), django.core.validators.MaxLengthValidator(100, message='Full name cannot exceed 100 characters.'), django.core.validators.RegexValidator(code='invalid_full_name', message='Full name must contain only alphabets and spaces.', regex='^[a-zA-Z ]+$')]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]