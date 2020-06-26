from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class StudentProfile(models.Model):
    GENDER_MALE = [
        ('Male', "Male"),
        ('Female', "Female"),
        ('Other', "Other"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_roll = models.IntegerField(default=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="student_profile", default="ques.png")
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.today)
    gender = models.CharField(choices=GENDER_MALE, max_length=10)
    about = models.TextField()
    status = models.BooleanField(default=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    address = models.TextField()
    mobile = models.CharField(default="", max_length=12)

    def __str__(self):
        return self.user.username


def create_student_profile(sender, created, instance, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)


post_save.connect(create_student_profile, sender=User)
