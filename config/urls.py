"""URL configuration for config project."""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Keep old bookmarks working; preserve POST bodies during redirects.
    path("index.html", RedirectView.as_view(pattern_name="home", permanent=True, query_string=True, preserve_request=True)),
    path("catalog.html", RedirectView.as_view(pattern_name="catalog", permanent=True, query_string=True, preserve_request=True)),
    path("favorites.html", RedirectView.as_view(pattern_name="favorites", permanent=True, query_string=True, preserve_request=True)),
    path("orders.html", RedirectView.as_view(pattern_name="orders", permanent=True, query_string=True, preserve_request=True)),
    path("profile.html", RedirectView.as_view(pattern_name="user_profile", permanent=True, query_string=True, preserve_request=True)),
    path("seller.html", RedirectView.as_view(pattern_name="seller", permanent=True, query_string=True, preserve_request=True)),
    path("contacts.html", RedirectView.as_view(pattern_name="contacts", permanent=True, query_string=True, preserve_request=True)),

    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("catalog.urls")),
    path("", include("favorites.urls")),
    path("", include("orders.urls")),
    path("", include("user_profile.urls")),
    path("", include("seller.urls")),
    path("", include("contacts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
