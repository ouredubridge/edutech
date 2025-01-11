from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.community, name='community'),
    path('group-list', views.group_list, name='group_list'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
]