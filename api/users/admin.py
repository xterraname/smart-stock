from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin

from api.users.models import MyUser

admin.site.unregister(Group)

@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    list_display = ["phone_number", "full_name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["phone_number", "password"]}),
        ("Personal info", {"fields": ["full_name"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone_number", "full_number", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["phone_number"]
    ordering = ["phone_number"]
    filter_horizontal = []