

from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()


    instructor =models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='course'
    )

    created_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title



class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name ="lessons"
    )

    subtitle=models.CharField(max_length=300)
    description = models.TextField(blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subtitle
