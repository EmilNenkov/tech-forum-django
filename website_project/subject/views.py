from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldError
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from website_project.web.forms import TopicForm
from website_project.web.models import Subject, CustomUser, Topic, Comment

class SubjectView(View):
    def get(self, request, title):
        subject = get_object_or_404(Subject, title=title)
        topics = subject.topic_set.all()
        topics_count = subject.topic_set.count()
        users_count = CustomUser.objects.filter(topic__subject__title=title).distinct().count()
        last_user = CustomUser.objects.get_latest_user()
        comment_count = Comment.objects.filter(topic__subject=subject).count()
        topics_with_replies_counts = Topic.objects.filter(subject=subject).annotate(reply_count=Count('comment'))
        post_count = comment_count + topics_count
    
        context = {
            'subject': subject,
            'topics': topics,
            'topics_count': topics_count,
            'users_count': users_count,
            'last_user': last_user,
            'total_posts_count': post_count,
            'topics_with_post_counts': topics_with_replies_counts
        }

        return render(request, 'common/subject.html', context)


@login_required
def start_discussion(request, title_name):
    subject = get_object_or_404(Subject, title=title_name)

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.subject = subject
            topic.user = request.user

            topic.save()
            return redirect('subject:subject-category', title=title_name, category=request.GET.get('category'))

    else:
        form = TopicForm()

    context = {
        'form': form,
        'subject': subject
    }

    return render(request, 'start_discussion.html', context)











