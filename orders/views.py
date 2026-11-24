from django.shortcuts import render


def orders(request):
    """Страница «Заказы»."""
    return render(request, "orders/orders.html")
