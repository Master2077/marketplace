from django.urls import path

from . import views

urlpatterns = [
    path("favorites.html", views.favorites, name="favorites"),
]
