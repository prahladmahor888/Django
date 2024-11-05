from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForms
from .models import createuser
import random


# Create your views here.

def home(request):
    if request.method == "POST":
        image = request.FILES['file']

    return render(request, "home.html")

def docs(request):
    return render(request, "docs.html")

def examples(request):
    return render(request, "example.html")

def user_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        user_id = random.randint(11111111111, 99999999999)
        user = User.objects.create_user(username, email, password)
        user.first_name = name
        user.save()
        user = createuser(user_id=user_id, name=name, phone=phone, email=email, password=password)
        user.save()
        return redirect("login")
        
    
    return render(request, "signup.html")

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have logged in!")
            return render(request, "home.html")
        else:
            messages.success(request, "Login Failed try again")
            return redirect("login")

    return render(request, "login.html", {})

def reset_pass(request):
    if request.method == 'POST':
        username = request.POST['username']
        return render(request, "newpassword.html", {'username': username})
    return render(request, "reset.html")

def about(request):
    return render(request, "about.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def new_pass(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if (password == repassword):
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return render(request, "login.html", {"msg": True})
    else:
        return render(request, "newpassword.html", {"msg": True})