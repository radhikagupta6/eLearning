
from django.urls import path
from . import views as ac_views
urlpatterns = [
    path('login/', ac_views.login_view, name="login"),
    path('signup/', ac_views.signup_view, name="signup"),
    path('', ac_views.dashboard, name="dashboard"),
    path('logout/', ac_views.logout_view, name="logout"),
    path('profile/', ac_views.profile_view, name="profile"),
    path('profile_edit/', ac_views.profile_edit, name="profile_edit"),
    path('change_password/', ac_views.change_password, name="change_password"),
]
