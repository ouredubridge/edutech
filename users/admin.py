from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomerUserAdmin(UserAdmin):
    #form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = CustomUser

    # Ensure search_fields use fields that exist in your CustomUser model
    search_fields = ('email', 'first_name', 'last_name')

    ordering = ['email']
    list_display = ['email', 'fullname', 'is_staff', ]

    #list_display = ['email', 'fullname', 'is_staff', ] 

    # Update fieldsets to remove references to username
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        #('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Also, if you have any add_fieldsets, update them as well
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

# Register your models here.
admin.site.register(CustomUser, CustomerUserAdmin)
#admin.site.register(CustomUser)