from django.test import TestCase
from community.models import Group

class CommunityPermissionTest(TestCase):
    def setUp(self):
        # Create a group
        self.group = Group.objects.create(name="Test Group", description="A test group")

    def test_unauthorized_access(self):
        # Test group list (should redirect to login)
        response = self.client.get(reverse('group_list'))
        self.assertNotEqual(response.status_code, 200)