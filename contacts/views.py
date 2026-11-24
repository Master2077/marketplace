from django.shortcuts import render

from .forms import ContactForm


def contacts(request):
    """Страница «Контакты» и обработка формы обратной связи."""
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(
        request,
        "contacts/contacts.html",
        {"form": form, "success": success},
    )
