from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Query
from courses.models import Course,Lesson,LessonProgress

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
               return redirect("accounts:instructor_dashboard")
           
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

    total_course=0
    completed_courses = 0
    ongoing_courses =0
    pending_courses =0

    courses = Course.objects.all()
     
    user=request.user
    enrollments = user.Enrollment.all()
    total_course=enrollments.count()
    for enrollment in enrollments:
        course = enrollment.course
        total_lessons = course.lessons.count()

        completed_lessons = LessonProgress.objects.filter(
        student = request.user,
        completed =True,
        lesson__course = course,
        ).count()

        if total_lessons > 0 and completed_lessons == total_lessons:
            completed_courses+=1
        elif completed_lessons > 0:
            ongoing_courses+=1
        else:
            pending_courses+=1
        




    return render(
        request,
        "student/dashboard.html",
        {
            "courses":courses,
         "completed_courses":completed_courses,
         "ongoing_courses":ongoing_courses,
         "pending_courses" : pending_courses,
         "total_course" : total_course
    }
    )

@login_required
def instructor_dashboard(request):
    courses = Course.objects.filter(instructor = request.user)

    total_courses = courses.count()
    total_lessons = Lesson.objects.filter(course__in = courses).count()
    total_students =Profile.objects.filter(role = "Student").count()

    return render(request,"instructor/dashboard.html",
                  {
                      "total_courses":total_courses,
                      "total_lessons":total_lessons,
                      "total_students":total_students,
                  })


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
