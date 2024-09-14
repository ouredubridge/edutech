from django.test import LiveServerTestCase
from django.test import TestCase
from django.contrib.auth.models import User
from users.models import CustomUser
from django.urls import reverse
from django.core import mail

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

class PasswordResetInvalidEmailTests(TestCase):

    def test_invalid_email_submission(self):
        response = self.client.post(reverse('password_reset'), {'email': 'invalidemail@example.com'})
        self.assertEqual(response.status_code, 302) # Should redirect to password reset done
        self.assertRedirects(response, reverse('password_reset_done'))
        self.assertEqual(len(mail.outbox), 0) # No email should be sent


class PasswordResetValidEmailTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(fullname="testuser newuser", email='testuser@gmail.com', password='testuser123')

    def test_valid_email_submission(self):
        response = self.client.post(reverse('password_reset'), {'email': self.user.email})

        self.assertEqual(response.status_code, 302) # Should redirect to password reset done
        self.assertRedirects(response, reverse('password_reset_done'))
        self.assertEqual(len(mail.outbox), 1) # One(1) email should be sent

class PasswordResetEmailTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(fullname="Test NewUser", email='test@example.com', password="oldpassword")

    def test_password_reset_email_contains_correct_link(self):
        # Trigger password reset email
        self.client.post(reverse('password_reset'), {'email': self.user.email})

        # Get the email sent
        email = mail.outbox[0]

        # Check the subject and recipient
        self.assertIn('Password reset', email.subject)
        self.assertIn(self.user.email, email.to)

        # Check that the reset link contains the uid64 and token
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.assertIn(f'/reset/{uidb64}/', email.body)


class PasswordResetConfirmTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(fullname="Test NewUser", email="test@example.com", password="oldpassword")

    def test_valid_token_renders_reset_form(self):
        # Generate valid uidb64 and token
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)

        # Send GET request to password reset confirm view
        response = self.client.get(reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token}))

        # If there's a redirect, check the status code and where it redirects to
        self.assertEqual(response.status_code, 302)
        self.assertIn('/reset/', response.url)
        self.assertIn('set-password', response.url)