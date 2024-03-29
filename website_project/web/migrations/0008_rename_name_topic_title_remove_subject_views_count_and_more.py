# Generated by Django 4.2.3 on 2023-07-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_topic_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='views_count',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(default='', max_length=335),
        ),
    ]
