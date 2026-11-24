from django.shortcuts import render


def index(request):
    """Страница «Главная»."""
    return render(request, "home/index.html")
