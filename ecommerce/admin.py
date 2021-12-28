from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_filter = ['c_name']
    list_display = ['c_name', 'c_email', 'c_phone', 'c_address']
    search_fields = ['c_name']
