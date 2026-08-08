from django.urls import path
from . import views
app_name =  "course"

urlpatterns = [

    path(
        "create/",
        views.create_course,
        name="create_course"
    ),
    path(
        "<int:course_id>/",
         views.course_detail,
        name="course_detail"
    ),
    path(
        "<int:lesson_id>",
        views.lesson_detail,
        name="lesson_detail"
    ),
     path("<int:course_id>/add-lesson/",
             views.add_lesson,
             name="add_lesson"),
]