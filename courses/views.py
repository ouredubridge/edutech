from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from django.http import HttpResponseForbidden

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