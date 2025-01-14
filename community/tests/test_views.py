from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from community.models import Group, Membership, Post


class CommunityViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = CustomUser.objects.create_user(
            fullname = 'Test Newuser',
            email='testuser@gmail.com',
            password='testpassword'
        )

        self.client.login(email='testuser@gmail.com', password='testpassword')

        # Create a group for the user
        self.group = Group.objects.create(
            name="Test Group",
            description="A test group"
        )

    def test_group_list_view(self):
        response = self.client.get(reverse('group_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/group_list.html')
        self.assertContains(response, "Test Group")

    def test_group_detail_view(self):
        response = self.client.get(reverse('group_detail', args=[self.group.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/group_detail.html')
        self.assertContains(response, "Test Group")