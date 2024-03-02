from django.urls import path, re_path
from website_project.subject import views

app_name = 'subject'

urlpatterns = [
    path('<str:title_name>/start-discussion/', views.start_discussion, name='start discussion'),
    re_path(r'^(?P<title>[\w-]+)/$', views.SubjectView.as_view(), name='subject'),
    # re_path(r'^(?P<title>[\w-]+)/(?P<category>[\w\s&()-]*)/$', views.SubjectView.as_view(), name='subject-category'),
    # re_path(r'^(?P<title>[\w-]+)/(?P<category>[\w\s&()-]*)/(?P<filter>[\w-]*)/$', views.SubjectView.as_view(), name='subject-category-filter'),
]
