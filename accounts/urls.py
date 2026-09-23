from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_accounts, name='list_accounts'),
    path('signup/', views.signup, name='signup'),
    path('', views.login_user, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>', views.edit_profile, name='profile'),
]
