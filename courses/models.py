from django.db import models
from users.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field
from tinymce.models import HTMLField

from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
class Course(models.Model):
    FREE = 'free'
    PAID = 'paid'
    SUBSCRIPTION = 'subscription'

    STATUS_CHOICES = [
        (FREE, 'Free'),
        (PAID, 'Paid'),
        (SUBSCRIPTION, 'Subscription')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses')
    published_date = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(CustomUser, related_name='enrolled_courses')

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=FREE)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']


    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    content = HTMLField()
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.course.title} - {self.module.order} {self.module.title} - {self.module.order}.{self.order} {self.title}"

class Enrollment(models.Model):
    choices=[
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=choices)
    progress = models.IntegerField(default=0)
    enrollment_date = models.DateTimeField(auto_now_add=True)