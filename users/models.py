from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
                
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Create and return a superuser with an email and password.

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True. ')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields) 

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    #username = models.CharField(max_length=150, blank=True, null=True, unique=True, default=None)
    email = models.EmailField(unique=True) 
    fullname = models.CharField(max_length=200)
    # Other fields (e.g., first_name, last_name)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    #username = models.CharField(max_length=150, unique=True, blank=True)

    """def get_username(self):
        return self.email"""