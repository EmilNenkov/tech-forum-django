from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from website_project.web.models import CustomUser, Topic


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'website', 'about']


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']


class ProfileEditForm(UserRegistrationForm):
    pass


