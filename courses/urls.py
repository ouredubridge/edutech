from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('create-course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/create-module/', views.create_module, name='create_module'),
    path('module/<int:module_id>/create-lesson/', views.create_lesson, name='create_lesson'),
    path('course/<int:course_id>/edit/', views.edit_course, name='edit_course'),
]