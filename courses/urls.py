from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('create-course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/create-module/', views.create_module, name='create_module'),
    path('module/<int:module_id>/create-lesson/', views.create_lesson, name='create_lesson'),
    path('course/<slug:course_slug>/edit/', views.edit_course, name='edit_course'),
    path('module/<int:module_id>/edit/', views.edit_module, name='edit_module'),
    path('lesson/<int:lesson_id>/edit/', views.edit_lesson, name='edit_lesson'),
    path('category/<int:category_id>/', views.filter_courses_by_category, name='filter_courses_by_category'),
]