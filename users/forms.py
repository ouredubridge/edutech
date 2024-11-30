from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fullname = forms.CharField(
        max_length=100,
        required=True,
        label="Full Name"
    )
    
    class Meta:
        model = CustomUser
        fields = ('email', 'fullname', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean() # Get the data from the parent class
        fullname = cleaned_data.get('fullname')

        # Perform custom validation on fullname
        if fullname:
            if len(fullname.strip()) < 4:
                self.add_error('fullname', "Full name must be at least 4 characters long.")
            if not fullname.replace(" ", "").isalpha():
                self.add_error('fullname', "Full name can only contain alphabetic characters")

        else:
            self.add_error('fullname', "Full name is required.")

        # Return the cleaned_data dictionary
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("Invalid email or password.")

            elif not self.user.is_active:
                raise forms.ValidationError("This account is inactive. ")

        return self.cleaned_data

    def get_user(self):
        return self.user