from django.urls import path
from . import views
app_name =  "course"

urlpatterns = [

    path(
        "create/",
        views.create_course,
        name="create_course"
    )
]