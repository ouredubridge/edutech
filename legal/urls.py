from django.urls import path
from .views import cookies_policy_page
from .views import privacy_policy_page
from .views import terms_of_services_page

urlpatterns = [
    path('cookies_policy', cookies_policy_page, name='cookies_policy'),
    path('privacy_polcy', privacy_policy_page, name='privacy_policy'),
    path('terms_of_services', terms_of_services_page, name='terms_of_services'),
]
