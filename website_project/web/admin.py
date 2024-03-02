from django.contrib import admin
from .forms import TopicForm
from .models import Subject, CustomUser, Topic


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


# Create a custom admin class for Topic
class TopicAdmin(admin.ModelAdmin):
    form = TopicForm


@admin.register(Topic)
class TopicAdminWithForm(TopicAdmin):
    pass
