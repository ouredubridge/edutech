from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from community.models import Group, Membership, Post


class CommunityViewTest(TestCase):
    # Create a user and log them in
    self.user = CustomUser.objects.create_user(
        fullname = 'Test Newuser',
        username='testuser',
        password='testpassword'
    )

    # Create a group for the user
    self.group = Group.objects.create(
        name="Test Group",
        description="A test group"
    )