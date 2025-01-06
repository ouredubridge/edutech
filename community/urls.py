from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.community, name='community'),
    path('group-list', views.group_list, name='group_list')
]