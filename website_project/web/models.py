from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, URLValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
import re
from website_project import settings
from website_project.managers import CustomUserManager
import time

class CustomUser(AbstractUser):
    full_name = models.CharField(
        default='',
        max_length=100,
        validators=[
            MinLengthValidator(4, message='Full name must be at least 4 characters long.'),
            MaxLengthValidator(100, message='Full name cannot exceed 100 characters.'),
            RegexValidator(
                regex=r'^[a-zA-Z ]+$',
                message='Full name must contain only alphabets and spaces.',
                code='invalid_full_name'
            )
        ]
    )

    about = models.TextField(
        max_length=300, null=True, blank=True
    )
    
    website = models.URLField(
        max_length=200, blank=True, null=True,
        validators=[URLValidator()]
    )

    email = models.EmailField(
        max_length=255, blank=True, null=True,
        validators=[EmailValidator()]
    )

    #  profile_pic = models.ImageField(upload_to='images/', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Subject(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        modded_title = self.title
        if '-' in modded_title:
            title_args = modded_title.split('-')
            title_args[0] = title_args[0].capitalize()
            title_args[1] = title_args[1].capitalize()
            modded_title = title_args[0] + ' ' + title_args[1]
        else:
            modded_title = modded_title.capitalize()

        return modded_title


class Topic(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=4_000, default='')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)
    time_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)

    def increment_views(self):
        time.sleep(5)
        self.views_count += 1
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    contents = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)









