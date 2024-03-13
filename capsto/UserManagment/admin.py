
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')  # Add or remove fields as needed
    list_filter = ('role',)  # Add or remove filters as needed

admin.site.register(CustomUser, CustomUserAdmin)
