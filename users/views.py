from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy

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
            # form.save()
            return redirect('home')

        else:
            # Handle form errors here
            form_errors = form.errors
    else:
        form = CustomUserCreationForm()
        form_errors = None

    return render(request, 'users/signup.html', {'form': form, 'form_errors': form_errors})


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
            next_url = request.GET.get('next') or reverse('home')

            # Authenticate user
            user = form.get_user()

            if user is not None:
                # login user
                login(request, user)

                # Check if a next URL is stored
                #if next_url:
                return redirect(next_url)
                #return redirect('home')

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
