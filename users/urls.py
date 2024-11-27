from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-account/', views.delete_account, name='delete-account'),
]
