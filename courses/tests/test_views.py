from django.test import TestCase
from django.urls import reverse

from courses.models import Category, Course
from users.models import CustomUser
from courses.views import course_list, course_detail


class CourseViewTests(TestCase):

    def test_course_list_view(self):

        # Create a sample course object
        """course = Course.objects.create(
            title="Introduction to Django",
            description="Learn the basics of django",
            category=Category.objects.create(name="Programming", description="Learn how to program"),
            instructor=CustomUser.objects.create(fullname="Test User", email="testuser123")
        )"""
        course = Course.objects.all()

        # Make a GET request to the course detail view
        response = self.client.get(f"/courses/")

        # Assert that the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is rendered
        self.assertTemplateUsed(response, "courses/course_list.html")

        # Assert that the course object is in the context
        #self.assertIn(course, response.context['course'])

    def test_course_detail_view(self):

        # Create a sample course object
        course = Course.objects.create(
            title="Introduction to Django",
            description="Learn the basics of django",
            category=Category.objects.create(name="Programming", description="Learn how to program"),
            instructor=CustomUser.objects.create(fullname="Test User", email="testuser123")
        )

        # Make a GET request to the course detail view
        response = self.client.get(f"/courses/{course.id}/")

        # Assert that the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is rendered
        self.assertTemplateUsed(response, "courses/course_detail.html")

        # Assert that the course object is in the context
        #self.assertIn(course, response.context['course'])