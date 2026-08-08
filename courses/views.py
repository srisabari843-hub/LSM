from django.shortcuts import render,redirect,get_object_or_404
from .models import Course,Lesson


def create_course(request):
    if request.method == "POST":
        name=request.POST["name"]
        desc=request.POST["description"]


        Course.objects.create(
            instructor = request.user,
            title=name,
            description = desc
        )

        return redirect("course:create_course")

    return render(request,"courses/create_course.html")


def course_detail(request,course_id):
    course=get_object_or_404(Course,id=course_id)
    return render(request,"courses/course_detail.html",
                  {
                    "course":course
                  })


def lesson_detail(request,lesson_id):
    lesson = get_object_or_404(Lesson,id=lesson_id)

    return render(
        request,
        'courses/lesson_detail.html',
        {
            'lesson':lesson
        }
    )


def add_lesson(request,course_id):
    course = get_object_or_404(Course,id=course_id)

    if request.method == "POST":
        subtitle=request.POST["subtitle"]
        description = request.POST["description"]
        video =request.FILES["video"]

        Lesson.objects.create(
            course=course,
            subtitle=subtitle,
            description = description,
            video = video
        )

        return redirect(
            "courses:course_detail",
            course_id = course.id
        )
    return render(
        request,
        "course/add_lesson.html",
        {"course":course}
    )