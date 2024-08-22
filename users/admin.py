from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomerUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'fullname', 'is_staff', ] 

# Register your models here.
admin.site.register(CustomUser, CustomerUserAdmin)