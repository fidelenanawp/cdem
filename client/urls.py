from django.contrib import admin
from django.urls import path
from client import views
urlpatterns = [
    path('check/<str:qrcode>', views.check_code, name='check'),
    path('list/<str:event_location>', views.list, name='list'),
    path('check/norecord/', views.norecord, name='norecord'),
    path('search/',views.check_code, name='search'),
    path('home/',views.home, name='home'),
    path("validate/<int:pk>", views.client_validate, name="client_validate"),
    path("details/<int:pk>", views.details, name="details"),
]