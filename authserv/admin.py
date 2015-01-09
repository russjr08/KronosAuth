from django.contrib import admin

from uuid import uuid4

# Register your models here.
from authserv.models import User

def disable_account(modeladmin, request, queryset):
    queryset.update(disabled=True)

def enable_account(modeladmin, request, queryset):
    queryset.update(disabled=False)

def generate_uuid(modeladmin, request, queryset):
    for user in queryset:
        user.generate_uuid()
        user.save()

disable_account.short_description = 'Disable selected Users'
enable_account.short_description = 'Enable selected Users'
generate_uuid.short_description = 'Generate new UUIDs for Users'

class UserAdmin(admin.ModelAdmin):
    actions = [disable_account, enable_account, generate_uuid]
    list_display = ('username', 'account_active', 'uuid')

admin.site.register(User, UserAdmin)
