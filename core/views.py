from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactUsForm

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

            # Provide feedback to the user
            return render(request, 'core/contact_success.html', {'form': form, 'success': 'Email successfully sent'})

    else:
        form = ContactUsForm()

    return render(request, 'core/home.html', {'form': form})
