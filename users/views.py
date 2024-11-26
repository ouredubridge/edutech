from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.views import View

from django.contrib.auth.decorators import login_required

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
            user.backend = 'email'
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
                messages.success(request, 'Login successfull!')

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


class CustomPasswordResetView(PasswordResetView):
    # Your password reset form template
    template_name = 'registration/password_reset_form.html'

    # Your email template
    email_template_name = 'registration/password_reset_email.html'

    # Redirect URL after form submission
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        # Capture the user's email and store it in the session
        email = form.cleaned_data.get('email')
        self.request.session['reset_email'] = email
        return super().form_valid(form)

class ResendPasswordResetEmailView(View):

    def get(self, request, *args, **kwargs):
        email = request.session.get('reset_email')

        if email:
            # Resend the password reset email
            form = PasswordResetForm({'email': email})

            if form.is_valid():
                form.save(
                    request=request,
                    use_https=request.is_secure(),
                    email_template_name='registration/password_reset_email.html'
                )

                messages.success(request, 'Password reset email resent successfully.')

            else:
                messages.error(request, 'There was a problem resending the email.')

        return redirect(reverse_lazy('password_reset_done'))

# Delete Account View
@login_required
def delete_account(request):
    if request.method == 'POST':
        # Delete the users's account
        user = request.user
        user.delete()
        messages.success(request, "Your account has been successfully deleted.")

    return render(request, 'users/delete_account.html')