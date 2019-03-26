from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('first_name', 'last_name', 'username', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {
            "fields": (
                'first_name',
                'last_name',
                'username',
                'email',
                'password'
            ),
        }),
        ('permissions', {
            'fields': ('is_admin',)
        })
    )

    search_fields = ('username', 'email')

    ordering = ('username', 'email')

    filter_horizontal = ()


admin.site.register(User, UserAdmin)


admin.site.unregister(Group)
