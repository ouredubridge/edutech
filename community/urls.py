from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.community, name='community'),
    path('group-list', views.group_list, name='group_list'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('group/<int:group_id>/join/', views.join_group, name='join_group'),
    path('group/<int:group_id>/create_post/', views.create_post, name='create_post'),
]