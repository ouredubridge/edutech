from django.shortcuts import render

# Create your views here.
def pricing_page(request):
    return render(request, 'payments/pricing.html')