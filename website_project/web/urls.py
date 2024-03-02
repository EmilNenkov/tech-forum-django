from django.urls import path, include, re_path
from website_project.web import views

handler404 = views.custom_404_view

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('register/', views.RegisterView().register_user, name='register'),
    path('login/', views.LoginView().login_view, name='login'),
    path('logout/', views.LogoutView().logout_view, name='logout'),
    path('', include('website_project.subject.urls')),
    path('@<str:username>/', include('website_project.account.urls'))
]