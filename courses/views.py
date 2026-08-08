from django.shortcuts import render

def create_course(request):

    return render(
        request,
        "courses/create_course.html"
    )
