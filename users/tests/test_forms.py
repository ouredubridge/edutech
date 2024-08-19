from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm

class SignupFormTest(TestCase):
    def test_signup_form_valid_data(self):
        form = CustomUserCreationForm(data = {
            'fullname': 'testuser newuser',
            'email': 'testuser@gmail.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertTrue(form.is_valid())
