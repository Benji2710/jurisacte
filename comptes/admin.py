from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Utilisateur


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Cabinet", {"fields": ("role",)}),)
    list_display = ("username", "first_name", "last_name", "role", "is_active")