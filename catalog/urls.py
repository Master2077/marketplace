from django.urls import path

from . import views

urlpatterns = [
    path("catalog.html", views.catalog, name="catalog"),
]
