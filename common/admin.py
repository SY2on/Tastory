from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
# Register your models here.


# class ProfileAdmin(admin.StackedInline):
#     model = Profile
#     con_delete = False


# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileAdmin,)


# admin.site.register(User, CustomUserAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
