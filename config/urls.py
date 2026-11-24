"""URL configuration for config project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("catalog.urls")),
    path("", include("favorites.urls")),
    path("", include("orders.urls")),
    path("", include("user_profile.urls")),
    path("", include("seller.urls")),
    path("", include("contacts.urls")),
]
