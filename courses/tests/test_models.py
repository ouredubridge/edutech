from django.test import TestCase
from courses.models import Category, Course, Module, Lesson#, Enrollment
from users.models import CustomUser

class CategoryModelTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(
            name="Programming",
            description="Become a professional in coding",
        )

        self.assertEqual(category.description, "Become a professional in coding")


class CourseModelTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title="Learn Python",
            category=Category.objects.create(name="Programming", description="Learn how to program"),
            description="Learn the basics of Python",
            instructor=CustomUser.objects.create(fullname="Test User", email="testuser@gmail.com")
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Learn Python")
        self.assertTrue(isinstance(self.course, Course))

class ModuleModelTests(TestCase):

    def setUp(self):
        self.module = Module.objects.create(
            course = Course.objects.create(
                title="Learn Python",
                category=Category.objects.create(name="Programming", description="Learn how to program"),
                description="Learn the basics of Python",
                instructor=CustomUser.objects.create(fullname="Test User", email="testuser@gmail.com")
            ),
            title="Introduction to Python",
            description="Have an overview of what Python is all about",
            order=1,
        )

    def test_module_creation(self):
        self.assertEqual(self.module.title, "Introduction to Python")

class LessonModelTests(TestCase):

    def setUp(self):
        self.lesson = Lesson.objects.create(
            title="Variables and Datatypes",
            content="Variables are containers for values",
            order=1,
        )

    def test_lesson_creation(self):
        self.assertEqual(self.lesson.title, "Variables and Datatypes")