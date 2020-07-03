
from django.urls import path
from . import views
urlpatterns = [
    path('c/', views.all_courses_views, name="all_c"),
    path('onec/', views.one_courses_views, name="one_c"),
]
