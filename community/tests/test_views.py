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

    def test_join_group(self):
        response = self.client.post(reverse('join_group', args=[self.group.id]))
        self.assertEqual(response.status_code, 302) # Redirect after joining
        self.assertTrue(Membership.objects.filter(
            user=self.user,
            group=self.group).exists()
        )

    def test_create_post(self):
        post_data = {'content': 'This is a test post'}
        response = self.client.post(reverse('create_post', args=[self.group.id]), post_data)
        # Redirect after creating a post
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(
            content='This is a test post',
            group=self.group,
            author=self.user
        ).exists())