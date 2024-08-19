from django.test import TestCase
from django.urls import reverse

class SignupViewTest(TestCase):

    def test_signup_view_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_page_contains_correct_html(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Create Account')
