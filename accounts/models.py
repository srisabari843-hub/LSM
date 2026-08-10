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

    phone=models.CharField(max_length=15,blank=True)

        
    def __str__(self):
         return self.user.username


class Query(models.Model):
     user=models.ForeignKey(
          User,
          on_delete=models.CASCADE,
          related_name="contact_message"
     )
     message=models.TextField()

     def __str__(self):
          return f"{self.user.username}"
     