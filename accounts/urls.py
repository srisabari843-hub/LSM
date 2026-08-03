from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path("login/",views.login_view,name="login"),
    path("register/",views.register_view,name="register"),
    path("logout/",views.logout_view,name="logout"),
    path("profile/",views.profile_view,name="profile"),
    path("student/dashboard/",
         views.student_dashboard,
         name="student_dashboard",),
    path("instructor/dashborad/",
         views.instructor_dashboard,
         name="instructor_dashboard",),
]