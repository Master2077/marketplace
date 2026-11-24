from django.shortcuts import render


def favorites(request):
    """Страница «Избранное»."""
    return render(request, "favorites/favorites.html")
