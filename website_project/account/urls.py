from django.urls import path
from website_project.account import views

app_name = 'account'

urlpatterns = [
    path('', views.AccountView.as_view(), name='account-details'),
    path('edit-account/', views.AccountEdit.as_view(), name='account-edit')
]