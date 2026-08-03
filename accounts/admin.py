from django.contrib import admin
from .models import Profile,Query
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "user",
        "role",
        "phone",
        "image"
    )

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "user",
        "message"
    )