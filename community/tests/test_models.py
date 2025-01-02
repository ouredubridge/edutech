from django.test import TestCase
from users.models import CustomUser
from community.models import Group, Membership, Post, Comment

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

    def test_group_creation(self):
        self.assertEqual(self.group.name, "Test Group")
        self.assertEqual(self.group.description, "A test group")

    def test_membership_creation(self):
        self.assertEqual(self.membership.user, self.user)
        self.assertEqual(self.membership.group, self.group)

    def test_post_creation(self):
        self.assertEqual(self.post.content, "Test post content")
        self.assertEqual(self.post.group, self.group)
        self.assertEqual(self.post.author, self.user)

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, "Test comment")
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.user)