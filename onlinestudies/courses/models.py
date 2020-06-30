from django.db import models
from datetime import datetime


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="courses", default="c.png")
    video = models.FileField(upload_to="cvideo", default="v.mp4")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="topics", default="t.png")
    video = models.FileField(upload_to="tvideo", default="tv.mp4")
    datetime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
