from django.shortcuts import render,redirect,get_object_or_404
from .models import Course,Lesson,Enrollment,LessonProgress

    

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
    
    enrolled = Enrollment.objects.filter(
        student=request.user,
        course = course
    ).exists()

    lessons=course.lessons.all()

    completed_count = LessonProgress.objects.filter(
        student = request.user,
        lesson__course = course,
        completed =True
    ).count()

    total_lessons = lessons.count()

    if completed_count ==0:
        course_status = "Pending"
    elif completed_count == total_lessons:
        course_status = "Completed"
    else:
        course_status = "Ongoing"

    for lesson in lessons:
        lesson.student_progress = LessonProgress.objects.filter(
            student = request.user,
            lesson =lesson
        ).first()
        
    return render(     
        request,
        "courses/course_detail.html",
        {
            "user":request.user,
            "course":course,
            "enrolled":enrolled,
            "completed_count":completed_count,
            "total_lessons":total_lessons,
            "course_status":course_status,
            "lessons":lessons,
        }
    )



def lesson_detail(request,course_id,lesson_id):

    course=get_object_or_404(Course,id=course_id)
    lesson = get_object_or_404(
        Lesson,
        id=lesson_id,
        course = course
    )


    progress,created = LessonProgress.objects.get_or_create(
        student=request.user,
        lesson = lesson
    )
    

    if request.method == "POST":
       progress.completed = True
       progress.save()

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
                    "progress":progress
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


def enroll_course(request,course_id):
    course = get_object_or_404(Course,id = course_id)

    Enrollment.objects.get_or_create(
        student = request.user,
        course = course  
    )

    return redirect("courses:my_courses")


def my_courses(request):
    enrollments = Enrollment.objects.filter(
        student = request.user
    )

    return render(
       request,
       "courses/my_courses.html",
       {"enrollments":enrollments}
    )