from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in sucessfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in...")
            return redirect('home')
    
    return render(request, 'crm_website/home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Loggedout..')
    return redirect('home')

def register(request):
    return render(request, 'crm_website/register.html', {})