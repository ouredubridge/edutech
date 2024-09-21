from django.shortcuts import render

# Create your views here.
def pricing_page(request):
    return render(request, 'pricing.html')