from django.urls import path

from . import views

urlpatterns = [
    path("profile.html", views.profile, name="user_profile"),
]
