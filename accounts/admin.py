from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Si tu n'as pas ajouté de champs supplémentaires, tu peux t'arrêter ici
   # list_display = ['username', 'email', 'is_staff', 'is_active']

admin.site.register(CustomUser,UserAdmin)