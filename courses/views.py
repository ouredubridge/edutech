from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from django.http import HttpResponseForbidden

from .forms import CourseForm

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