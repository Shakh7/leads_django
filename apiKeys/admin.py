from django.contrib import admin

from .models import ApiKey


# Register your models here.

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'is_active',)
    list_filter = ('is_active',)


admin.site.register(ApiKey, ApiKeyAdmin)
