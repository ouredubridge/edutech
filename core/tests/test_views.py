from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):

    # Ensures the homepage URL returns a status code of 200 (OK).
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # Confirms the correct template is used for rendering the homepage
    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'core/home.html')

    # Checks that specific HTML content is present in the homepage
    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Welcome To <span>EduBridge</span></h1>')


    # Verifies that certain HTML content is not present in the homepage
    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Hi Kadel')

    # Verifies that the contact us form is found in the homepage
    def test_homepage_contains_contact_us_form(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Contact Us')
        self.assertContains(response, 'form')
        self.assertContains(response, 'input')

    # Ensures that the view passes the correct context data to the template
