from django.test import TestCase
from users.models import CustomUser
from community.models import Group, Membership, Post, CommunityPageTests

class CommunityModelTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(
            fullname="Newuser Testuser",
            email="testuser@gmail.com",
            password="testpassword"
        )

        # Create a group
        self.group = Group.objects.create(name="Test Group", description="A test group")

        # Create a membership
        self.membership = Membership.objects.create(user=self.user, group=self.group)

        # Create a post
        self.post = Post.objects.create(group=self.group, author=self.user, content="Test post content")

        # Create a comment
        self.comment = Comment.objects.create(post=self.post, author=self.user, content="Test comment")