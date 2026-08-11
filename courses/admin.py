from django.contrib import admin
from .models import Course,Lesson,LessonProgress

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


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display=[
        "student",
        "lesson",
        "completed"
    ]