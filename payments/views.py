

from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from .models import Course, Payment

# Create your views here.

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def pricing_page(request):
    # Check if the request is an AJAX
    if is_ajax(request):
        return render(request, 'payments/partials/pricing_content.html')
    return render(request, 'payments/pricing.html') 

def cart_page(request):
    return render(request, 'payments/cart.html')

#def checkout_page(request):
 #   return render(request, 'payments/checkout.html')


def checkout_page(request):
    course = get_object_or_404#(course)
    host = request.get_host()   #for getting domain
    paypal_details = {
       'business': settings.PAYPAL_RECEIVER_EMAIL,
       'amount':     "course.price",
       'item_name': "course.title",
        'invoice': f"{uuid.uuid4()} - {request.user.id}" ,
        'currency_code': 'NGN',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}", #request.build_absolute_uri(reverse('paypal-ipn')),
        'return_url': f"http://{host}{reverse('payment_done')}", #request.build_absolute_uri(reverse('payment_done')),
        'cancel_url': f"http://{host}{reverse('payment_cancel')}", #request.build_absolute_uri(reverse('payment_cancel')),
    }
    
    form = PayPalPaymentsForm(initial=paypal_details)
    
    
    context = {
       'course': course,
        'form': form,
    }
    
    return render(request, 'payments/checkout.html', context)
  
def payment_done(request):
  return render(request, 'payments/payment_done.html')


def payment_cancel(request):
  return render(request, 'payments/payment_cancel.html')
