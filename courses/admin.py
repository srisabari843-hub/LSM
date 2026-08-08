from django.contrib import admin
from .models import Course,Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display=[
        "id",
        "title",
        "description",
        "instructor",
        "created_at",
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "course",
        "subtitle",
        "description",
        "created_at",
    ]
