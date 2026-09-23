from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    profil = models.CharField(max_length=50, blank=True, null=True)
