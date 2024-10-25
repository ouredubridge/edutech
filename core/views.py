from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactUsForm

# Import Course model
from courses.models import Course


from django.http import JsonResponse

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

# Create your views here.
def homepage(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Extract the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email content
            email_message = f"From: {name} <{email}>\n\n{message}"

            try:
                # Send the email
                send_mail(
                    subject=subject,
                    message=email_message,
                    from_email=email,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL]
                )

            except Exception as e:
                # Handle email sending failure
                print(e)
                return render(request, 'core/contact_success.html', {'form': form, 'error': 'Failed to send email.'})
            
            # For normal requests, render the full base template

            # Provide feedback to the user
            return render(request, 'core/contact_success.html', {'form': form, 'success': 'Email successfully sent'})
    
    else:
        form = ContactUsForm()
        course = Course.objects.all()

        if is_ajax(request):
                return render(request, 'core/partials/home_content.html', {'form': form })

    return render(request, 'core/home.html', {'form': form, 'course': course})

def about_us(request):
    # Check if it is an AJAX request
    if is_ajax(request):
        return render(request, 'core/partials/about_content.html')

    # For normal requests, render the full base template
    return render(request, 'core/about_us.html')