from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def teacher_login(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or another page
        else:
            # Handle invalid login
            pass

    return render(request, 'signin.html')

def teacher_signup(request):
    if request.method == 'POST':
        # Handle signup form submission using Django's built-in UserCreationForm
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_login')  # Redirect to the login page after signup

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})



# Create your views here.

def home(request):
    return render (request, "authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        newUsername = request.POST['newUsername']
        
        email = request.POST['email']
        newPassword = request.POST['newPassword']
        confirmPassword = request.POST['confirmPassword']
    
        myuser = User.objects.create_user(newUsername, email, newPassword)
        
        
        myuser.save()
        messages.success(request, "Created")
        
        return redirect('signin')
    
    
    return render(request, "authentication/index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password =pass1)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "authentication/index.html", {'firstname':firstname})
            
        else:
            messages.error(request, "Invalid credentials")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


def admilogin(request):
     
    return render(request, "authentication/admilogin.html")