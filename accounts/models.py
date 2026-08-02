from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES=[
        ("Student","Student"),
         ("Instructor","Instructor"),]

    user=models.OneToOneField(
             User,
             on_delete=models.CASCADE
         )

    role=models.CharField(
             max_length=20,
             choices=ROLE_CHOICES
         )
    
    image=models.ImageField(
         upload_to="profiles/",
         default="profiles/default.png"
    )

        
    def __str__(self):
         return self.user.username

