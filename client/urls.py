from django.contrib import admin
from django.urls import path
from client import views
urlpatterns = [
    path('check/<str:qrcode>', views.check_code, name='check'),
    path('list/<str:event_location>', views.list, name='list'),
]