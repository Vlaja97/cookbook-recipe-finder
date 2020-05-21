from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid(): # Checking if form is valid
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else: # If form is not valid it will still display form
            context['registration_form'] = form
    else: # GET Request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def login_view(request):
    context = {}
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})