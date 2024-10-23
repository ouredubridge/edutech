
import paypalrestsdk
from django.conf import settings
from django.shortcuts import redirect, render

#Configure Paypal SDK
paypalrestsdk.configure({
    'mode' : settings.PAYMENT_MODE,
    'client_id' : settings.PAYPAL_CLIENT_ID,
    'client_secret' : settings.PAYPAL_CLIENT_SECRET,
})

# Create your views here.
def pricing_page(request):
    return render(request, 'payments/pricing.html') 