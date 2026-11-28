from django.shortcuts import render
from .models import Product


def catalog(request):
    """Страница «Каталог»."""
    products = Product.objects.order_by('-created_at')[:5]

    for product in products:
        print(product.name)

    return render(request, "catalog/catalog.html")
