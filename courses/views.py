from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Module, Lesson, Enrollment
from django.http import HttpResponseForbidden

from .forms import CourseForm, ModuleForm, LessonForm

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required(login_url="/login/")
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if course.status == Course.PAID:
        # Check if the user has paid for the course
        if not Enrollment.objects.filter(user=request.user, course=course, is_paid=True).exists():
            return HttpResponseForbidden("You do not have access to this course")

    return render(request, 'courses/course_detail.html', {'course': course})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user # Set the current user as the instructor
            course.save()
            return redirect('course_list')

    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

# View for creating a module for a course
def create_module(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = ModuleForm(request.POST)

        if form.is_valid():
            module = form.save(commit=False)
            module.course = course # Link the module to the course
            module.save()
            return redirect('course_detail', course_id=course.id)

    else:
        form = ModuleForm()

    return render(request, 'courses/create_module.html', {'form': form, 'course': course})


# View for creating a lesson for a module
def create_lesson(request, module_id):
    module = Module.objects.get(id=module_id)

    if request.method == 'POST':
        form = LessonForm(request.POST)

        if form.is_valid():
            lesson = form.save(commit=False)

            # Link the lesson to the module
            lesson.module = module

            # Save the lesson
            lesson.save()

            return redirect('module_detail', module_id=module.id)

    else:
        form = LessonForm()
    return render(request, 'courses/create_lesson.html', {'form': form, 'module': module})

"""Views for Editing:
- Courses
- Modules
- Lessons
"""
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course.id)

    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})


# Edit Module
def edit_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)

        if form.is_valid():
            form.save()
            return redirect('module_detail', module_id=module.id)

    else:
        form = ModuleForm(instance=module)

    return render(request, 'courses/edit_module.html', {'form': form, 'module': module})

# Edit Lesson
def edit_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)

        if form.is_valid():
            form.save()

            # Redirect to lesson detail page
            return redirect('lesson_detail', lesson_id=lesson.id)

    else:
        form = LessonForm(instance=lesson)

    return render(request, 'courses/edit_lesson.html', {'form': form, 'lesson': lesson})