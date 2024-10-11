from django.test import TestCase
from django.urls import reverse


class CommunityPageTests(TestCase):

    # Ensures the community page returns the correct status code 200(OK)
    def test_community_status_code(self):
        response = self.client.get(reverse('community'))