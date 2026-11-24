from django.shortcuts import render


def seller(request):
    """Страница «Страница автора»."""
    return render(request, "seller/seller.html")
