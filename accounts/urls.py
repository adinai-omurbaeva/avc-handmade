from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('', views.account_info, name='account_info'),
]