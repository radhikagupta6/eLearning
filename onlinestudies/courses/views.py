from django.shortcuts import render, HttpResponse
from .models import Course


# Create your views here.

def all_courses_views(request):
    c = Course.objects.filter(status=True).order_by('-id')
    context = {
        'w': c
    }
    return render(request, 'all_course.html', context)


def one_courses_views(request):
    context = dict()
    if request.is_ajax():
        cid = request.GET.get('c_id')
        c = Course.objects.get(id=cid)

        context = {
            'course': c
        }
    return render(request, 'one_course.html', context)
