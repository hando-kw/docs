from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import HttpRequest

from .models import User, UserAddress, UserOtp

class UserCreationAdminForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].required = True

class UserChangeAdminForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].required = True

@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('fullname', 'mobile', 'email', 'password1', 'password2'),
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Extra Information', {
            'classes': ('wide',),
            'fields': ('date_joined', 'last_login'),
        })
    )
    fieldsets = (
        ('Personal info', {
            'fields': ('fullname', 'mobile', 'email', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Extra Information', {
            'fields': ('date_joined', 'last_login'),
        })
    )
    add_form = UserCreationAdminForm
    form = UserChangeAdminForm
    list_display = ('fullname', 'email', 'mobile', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('fullname', 'mobile')
    ordering = ('-date_joined',)

@admin.register(UserOtp)
class UserOtpAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'otp', 'created_at')
    search_fields = ('mobile',)

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'name', 'address_type')
    search_fields = ('user__fullname', 'user__mobile', 'city__name_en', 'city__name_ar')
    list_filter = ('address_type',)
    
    def has_delete_permission(self, request, obj=None):
        return False