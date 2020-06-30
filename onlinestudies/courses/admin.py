from django.contrib import admin
from .models import Course,Topic,Subject
# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Topic)
