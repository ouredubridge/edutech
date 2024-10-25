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

    def test_signup_redirects_after_POST(self):
        url = reverse('signup')
        data = {
            'fullname': 'testuser newuser',
            'email': 'testuser@gmail.com',
            'password': 'testuser123',
            'password1': 'testuser123',
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('home'), response.url)


# ***************
# Login View Test
# ***************
class LoginViewTest(TestCase):

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_page_contains_correct_html(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Create Account')

class PasswordResetViewTest(TestCase):

    def test_password_reset_form_renders(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')
        self.assertContains(response, 'name="email"')


# Test Password Reset Done Page
class PasswordResetDoneTests(TestCase):
    def test_password_reset_done_page_renders(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_done.html')