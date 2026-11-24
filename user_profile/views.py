from django.shortcuts import render


def profile(request):
    """Страница «Профиль»."""
    return render(request, "user_profile/profile.html")
