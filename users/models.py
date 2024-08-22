from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 

    # Other fields (e.g., first_name, last_name)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    #username = models.CharField(max_length=150, unique=True, blank=True)
    fullname = models.CharField(max_length=200)