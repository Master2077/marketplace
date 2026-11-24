from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Форма обратной связи на странице «Контакты»."""

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
