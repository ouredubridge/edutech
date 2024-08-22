from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            """
            fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = CustomUser.objects.create_user(fullname=fullname, email=email, password=password)
            """

            user = form.save()
            login(request, user)
            return redirect('home')

        else:
            # If the form is invalid, re-render the form with entered data
            return render(request, 'users/signup.html', {'form': form})
            # Store form data in session
            # request.session['registration_data'] = request.POST
    else:
        # Retrieve form data from session if available
        # initial_data = request.session.get('registration_data', {})

        form = CustomUserCreationForm()

        # Clear session data to prevent repopulation on subsequent requests
        # request.session.pop('registration_data', None)
    return render(request, 'users/signup.html', {'form': form})


"""The login view function

Keyword arguments:
request -- The request object
Return: The login template render
"""
def login_view(request):
    return render(request, 'users/login.html')
