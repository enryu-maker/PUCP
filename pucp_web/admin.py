from django.contrib import admin
from django.http import HttpRequest
from .models import UserData

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(UserData, UserAdmin)

# Register your models here.
