from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm

class SignupFormTest(TestCase):
    def test_signup_form_valid_data(self):
        form = CustomUserCreationForm(data = {
            'fullname': 'testuser newuser',
            'email': 'testuser@gmail.com',
            'password': 'newpassword123',
            'password1': 'newpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_data(self):
        form_data = {
            'fullname': '',
            'email': 'invalid_email',
            'password': '',
            'password1': 'invalid_password'
        }

        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
