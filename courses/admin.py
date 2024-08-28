from django.contrib import admin
from .models import Category, Course, Lesson, Subsection, Enrollment

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Subsection)
admin.site.register(Enrollment)