from django.urls import path

from . import views

urlpatterns = [
    path("seller.html", views.seller, name="seller"),
]
