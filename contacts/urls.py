from django.urls import path

from . import views

urlpatterns = [
    path("contacts.html", views.contacts, name="contacts"),
]
