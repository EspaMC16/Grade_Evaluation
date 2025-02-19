from django.shortcuts import render, redirect, get_object_or_404
import django.contrib.messages as messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User



def logged_out(request):
    logout(request)
    return render(request, "registration/logged_out.html")


def sign_up(request):
    """Register a new user."""
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if not password2:
            messages.error(request, "Password confirmation is required.")
            return redirect('users:sign_up')
        
        if password != password2:
            messages.error(request, "Password do not match.")
            return redirect('users:sign_up')
        
        user, created = User.objects.get_or_create(username=username, email=email)

        if created:
            # Sets the password.
            user.set_password(password)
            # Create the account as a student only
            user.is_staff = True
            # Save the username, email and password.
            user.save()
            messages.success(request, "")
            # Authenticate your user with unhashed password, because `authenticate` hashes it again
            authenticated_user = authenticate(username=username, password=password)
            # Log in the user's account
            login(request, authenticated_user)
            return render(request, 'grade_evaluation_system/home.html')
        
        else:
            messages.error(request, "User already exists. Please enter another username...")
            return redirect('users:sign_up')
        
    return render(request, 'registration/sign_up.html')


def login_user(request):
    """User log in"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user via uusername and password.
        user = authenticate(request, username=username, password=password)
        # If the username or password doesn't match; It will raise an error.
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('users:login')
        
        # If no error; the user will be logged in.
        login(request, user)
        messages.success(request, "")
        return render(request, 'grade_evaluation_system/home.html')
        
    return render(request, 'registration/login.html', {})


def admin_sign_up(request):
    """Register a new user."""
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if not password2:
            messages.error(request, "Password confirmation is required.")
            return redirect('users:admin_sign_up')
        
        if password != password2:
            messages.error(request, "Password do not match.")
            return redirect('users:admin_sign_up')
        
        user, created = User.objects.get_or_create(username=username, email=email)

        if created:
            # Sets the password.
            user.set_password(password)
            # Create account as admin
            user.is_superuser = True
            user.is_staff = True
            # Save the username, email and password.
            user.save()
            messages.success(request, "")
            # Authenticate your user with unhashed password, because `authenticate` hashes it again
            authenticated_user = authenticate(username=username, password=password)
            # Log in the user's account
            login(request, authenticated_user)
            return redirect('/admin')
        
        else:
            messages.error(request, "User already exists. Please enter another username...")
            return redirect('users:admin_sign_up')
        
    return render(request, 'registration/admin_sign_up.html')


def login_admin(request):
    """Admin log in"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate user via uusername and password.
        user = authenticate(request, username=username, password=password)
        # If the username or password doesn't match; It will raise an error.
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('users:login_admin')
        
        # If no error; the user will be logged in.
        login(request, user)
        return redirect('/admin')
        
    return render(request, 'registration/login_admin.html', {})