from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def register_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect("accounts:register")
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request,"Registration successful Please login")
        return redirect("accounts:login")
    return render(request,"accounts/register.html")


def login_view(request):
    if request.method=="POST":
       username=request.POST["username"]
       password=request.POST["password"]

       user=authenticate(
           request,
           username=username,
           password=password
       )
       if user is not None:
           login(request,user)
           return redirect("/")
       messages.error(request,"Invalid username or Passwords")
    return render(request,"accouts/login.html")
