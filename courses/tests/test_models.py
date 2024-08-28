from django.test import TestCase
from courses.models import Course, Category#, Enrollment
from users.models import CustomUser

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Introduction to Python",
            category=Category.objects.create(name="Programming", description="Learn how to program"),
            description="Learn the basics of Python",
            instructor="Kadel Code"
        )
        self.assertEqual(course.title, "Introduction to Python")

class CategoryModelTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(
            name="Programming",
            description="Become a professional in coding",
        )

        self.assertEqual(category.description, "Become a professional in coding")