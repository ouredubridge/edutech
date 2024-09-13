from django.test import LiveServerTestCase
from django.test import TestCase
from django.contrib.auth.models import User
from users.models import CustomUser
from django.urls import reverse
from django.core import mail

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