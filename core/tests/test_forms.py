from django.test import TestCase

from core.forms import ContactUsForm

class ContactUsFormTest(TestCase):
    def test_contact_form_valid(self):
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'subject': 'Test Subject',
            'message': 'An email test message.'
        }

        form = ContactUsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        # Test with invalid data (missing required fields)
        form_data = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }

        form = ContactUsForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

