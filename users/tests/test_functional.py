from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from django.test import TestCase
from django.contrib.auth.models import User
from users.models import CustomUser
from django.urls import reverse

class SignupTest(TestCase):
    def test_signup(self):
        # Define the signup data
        signup_data = {
            'fullname': 'testuser newuser',
            'email': 'testusernewuser@gmail.com',
            'password': 'testuser123',
            'password1': 'testuser123',
        }

        # Send a POST request to the signup view with the signup data
        response = self.client.post(reverse('signup'), signup_data)

        # Log the user in
        # self.client.login(email='testusernewuser@gmail.com', password='testuser123')

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Follow the redirect
        response.client.get(response.url)

        # Check if the user was created in the database
        self.assertTrue(CustomUser.objects.filter(email='testusernewuser@gmail.com').exists())

        # Check if the user is logged in
        #self.assertTrue(response.context['user'].is_authenticated)

class LoginLogoutTest(TestCase):
    def setUp(self):
        #self.username = "testuser"
        self.email = "testuser@gmail.com"
        self.password = "testuser123"
        self.user = CustomUser.objects.create_user(email=self.email, password=self.password)

    def test_login(self):
        # Send a POST request to the login view with the user's details
        response = self.client.post(reverse('login'), {
            'email': self.email,
            'password': self.password,
        })

        # Check if the response is a redirect (to the login page)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect
        response = self.client.get(response.url)

        # Check if the user is logged in
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        # Log in the user first
        self.client.login(email=self.email, password=self.password)

        # Send a GET request to the logout view
        response = self.client.get(reverse('logout'))

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Follow the redirect
        response = self.client.get(response.url)

        # Check if the user is logged out
        self.assertFalse(response.context['user'].is_authenticated)

class UsersFunctionalTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_register(self):
        # User opens the browser and goes to the signup page
        self.browser.get(self.live_server_url + '/register/')

        # User fills out the signup form
        fullname_input = self.browser.find_element(By.NAME, 'fullname')
        fullname_input.send_keys('testuser newuser')

        email_input = self.browser.find_element(By.NAME, 'email')
        email_input.send_keys('newuser@gmail.com')

        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys('testuser123')

        password_confirm_input = self.browser.find_element(By.NAME, 'password1')
        password_confirm_input.send_keys('testuser123')

        # User submits the form
        password_confirm_input.send_keys(Keys.RETURN)

        # The user is redirected to the login page
        login_text = self.browser.find_element(By.TAG_NAME, 'h3').text
        self.assertIn('Login', login_text)