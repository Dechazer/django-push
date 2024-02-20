from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    return render (request, "authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        
        myuser.save()
        messages.success(request, "Created")
        
        return redirect('signin')
    
    
    return render(request, "authentication/signup.html")

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


def admin(request):
     
    if request.method == 'POST':
        
        if request.POST.get('login_as_admin'):
            
            # If "Login as Admin" button is clicked
            admin_username = 'admin'
            admin_password = 'admin'

            user = authenticate(username=admin_username, password=admin_password)
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f"Logged in as {admin_username}")
                return redirect('admin:index')  # Redirect to the admin dashboard

    form = AuthenticationForm()
    return render(request, 'authentication/admin.html', {'form': form})