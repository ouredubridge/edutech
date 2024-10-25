from django.urls import path
from .views import pricing_page

urlpatterns = [
    path('pricing/', pricing_page, name='pricing_page')
]