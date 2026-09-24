from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_accounts, name='list_accounts'),
    path('adduser/', views.signup, name='adduser'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>', views.edit_profile, name='profile'),
]
