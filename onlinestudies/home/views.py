from django.shortcuts import render

# Create your views here.
from courses.models import Course


def homepage(request):

    return render(request, 'home/index.html')
