from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image', 'slug')
    search_fields = ('user', 'slug')


admin.site.register(Profile, ProfileAdmin)
