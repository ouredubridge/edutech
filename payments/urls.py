from django.urls import path
from .views import pricing_page
from .views import cart_page
from .views import checkout_page, payment_done , payment_cancel

urlpatterns = [
    path('pricing/', pricing_page, name='pricing_page'),
    path('cart/', cart_page, name='cart_page'),
    path('checkout/', checkout_page, name='checkout_page'),
    path('success/', payment_done, name='payment_done'),
    path('failed/', payment_cancel, name='payment_cancel'),
]