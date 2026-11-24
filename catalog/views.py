from django.shortcuts import render


def catalog(request):
    """Страница «Каталог»."""
    return render(request, "catalog/catalog.html")
