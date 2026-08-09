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

        return redirect("courses:create_course")

    return render(request,"courses/create_course.html")


def course_detail(request,course_id):
    course = get_object_or_404(Course,id = course_id)

    return render(
        request,
        "courses/course_detail.html",
        {
            "course":course
        }
    )



def lesson_detail(request,course_id,lesson_id):

    course=get_object_or_404(Course,id=course_id)
    lesson = get_object_or_404(
        Lesson,
        id=lesson_id,
        course = course
    )

    lessons = list(course.lessons.all().order_by("id"))
     
    current_index = lessons.index(lesson)

    previous_lesson =(
        lessons[current_index-1]
        if current_index > 0
        else None
    )

    next_lesson = (
        lessons[current_index+1]
        if current_index < len(lessons) -1
        else None
    )



    return render(request,"courses/lesson_detail.html",
                  {
                    "course":course,
                    "lesson" : lesson,
                    "previous_lesson":previous_lesson,
                    "next_lesson":next_lesson,
                  })




def add_lesson(request,course_id):
    course = get_object_or_404(Course,id=course_id)

    if request.method == "POST":
        subtitle=request.POST["subtitle"]
        description = request.POST["description"]
        video_url =request.POST.get("video_url")

        if "watch?v=" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[0]           
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]

        
        video_url = f"https://www.youtube.com/embed/{video_id}"


        

        Lesson.objects.create(
            course=course,
            subtitle=subtitle,
            description = description,
            video = video_url
        )

        return redirect(
            "courses:course_detail",
            course_id = course.id
        )
    
    return render(
        request,
        "courses/add_lesson.html",
        {"course":course}
    )