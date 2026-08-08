from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Query
from courses.models import Course

def register_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect("accounts:register")
        
        user=  User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(
         user=user,
         role=request.POST["role"]
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
           profile=user.profile
           if profile.role == "Student":
               return redirect("accounts:student_dashboard")
           else:
               return redirect("Accounts:instructor_dashboard")
           
       messages.error(request,"Invalid username or Passwords")
    return render(request,"accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def profile_view(request):
    profile=request.user.profile

    if request.method=="POST":
        if "image" in request.FILES:
            profile.image=request.FILES["image"]
            profile.save()
        return redirect("accounts:profile")
            
    return render(request,"accounts/profile.html",{
        "profile":profile,
    })


@login_required
def student_dashboard(request):
    return render(request,"student/dashboard.html")

@login_required
def instructor_dashboard(request):
    return render(request,"instructor/dashboard.html")


def about(request):
    return render(request,"about.html")



@login_required
def contact(request):
    if request.method == "POST":
        Query.objects.create(
            user=request.user,
            message= request.POST["message"]
        )
        return redirect("home")
    return render(request,"contact.html")


def instructor_courses(request):
    courses=Course.objects.filter(instructor =request.user)

    return render(
        request,
        "instructor/courses.html",
        {"courses":courses}
    )