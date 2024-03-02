from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from website_project.web.forms import UserRegistrationForm, LoginForm
from website_project.web.models import Subject, CustomUser


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


class IndexView(View):
    def get(self, request):
        subject_queryset = Subject.objects.all()

        total_posts = 0

        total_views_count = []
        topic_counts = []
        comment_counts = []

        subjects_with_topic_count = Subject.objects.annotate(topic_count=Count('topic'))
        subjects_with_comment_count = Subject.objects.annotate(
            topic_count=Count('topic'),
            comment_count=Count('topic__comment')
        )

        for index, subject in enumerate(subject_queryset):
            subject_total_views = subject.topic_set.aggregate(total_views=Sum('views_count'))['total_views']
            if subject_total_views:
                total_views_count.append(subject_total_views)
            else:
                total_views_count.append(0)
            topic_counts.append(subjects_with_topic_count[index].topic_count)
            comment_counts.append(subjects_with_comment_count[index].comment_count)
            total_posts += (topic_counts[index] + comment_counts[index])

        general_views, introduction_views, announcement_views, staff_disc_views = total_views_count[0:]
        general_topics, introduction_topics, announcement_topics, staff_disc_topics = topic_counts[0:]
        general_comments, introduction_comments, announcement_comments, staff_disc_comments = comment_counts[0:] 

        context = {
            'posts_count': total_posts,

            'general_topics_count': general_topics,
            'introduction_topics_count': introduction_topics,
            'announcement_topics_count': announcement_topics,
            'staff_disc_topics_count': staff_disc_topics,

            'general_comments_count': general_comments,
            'introduction_comments_count': introduction_comments,
            'announcement_comments_count': announcement_comments,
            'staff_disc_comments_count': staff_disc_comments,

            'general_views': general_views,
            'introduction_views': introduction_views,
            'announcement_views': announcement_views,
            'staff_disc_views': staff_disc_views,
        }

        return render(request, 'common/home.html', context)


class RegisterView:
    def register_user(self, request):
        #  if request.user.is_authenticated:
        #      return redirect('home')

        if request.method == "POST":
            form = UserRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You have successfully registered your account!")
                return redirect('home')
        else:
            form = UserRegistrationForm()

        return render(request, 'account/registration.html', {'form': form})


class LoginView:
    def login_view(self, request):
        #  if request.user.is_authenticated:
        #      return redirect('home')

        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


class LogoutView:
    def logout_view(self, request):
        if not request.user.is_authenticated:
            return redirect('home')

        logout(request)
        return redirect('home')
    