from django.shortcuts import render
from django.conf import settings

# Create your views here.
def cookies_policy_page(request):
    return render(request, 'legal/cookies-policy.html')


def privacy_policy_page(request):
    return render(request, 'legal/privacy-policy.html')

def terms_of_services_page(request):
    return render(request, 'legal/terms-of-services.html')