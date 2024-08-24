from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

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
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)

        if form.is_valid():
            #email = form.cleaned_data['email']
            #password = form.cleaned_data['password']

            # Authenticate user
            user = form.get_user()

            if user is not None:
                # login user
                login(request, user)
                return redirect('home')

        #else:
            #context = {'form': form, 'error_message': 'Invalid login credentials'}
            #return render(request, 'users/login.html', context)

    else:
        form = CustomUserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')
