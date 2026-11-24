from django.urls import path

from . import views

urlpatterns = [
    path("orders.html", views.orders, name="orders"),
]
