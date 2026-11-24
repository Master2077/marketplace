from django.db import models


class ContactMessage(models.Model):
    """Сообщение, отправленное через форму обратной связи."""

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Почта")
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Отправлено", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение с формы"
        verbose_name_plural = "Сообщения с формы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
