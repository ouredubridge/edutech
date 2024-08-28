from django.test import TestCase
from users.models import CustomUser

class CustomUserTests(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create(
            fullname = "Testuser Newuser",
            email = "testuser@gmail.com",
            password = "testpassword123"
        )

        self.assertEqual(user.fullname, "Testuser Newuser")
        self.assertEqual(user.email, "testuser@gmail.com")