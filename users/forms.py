from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    fullname = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'password']

    """def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        return username"""

    def clean(self):
        cleaned_data = super().clean()

        #email = self.cleaned_data['email']
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')

        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data

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