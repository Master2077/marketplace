from django.db import models
from django.db.models import PROTECT
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField("Категория", max_length=30, unique=True)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
        db_table = "category"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField("Описание")
    image = models.ImageField("Картинка", upload_to="catalog/products/")
    stock = models.PositiveIntegerField("Количество", default=0)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    updated_at = models.DateTimeField("Изменено", auto_now=True)
    is_active = models.BooleanField("Активен", default=True)
    slug = models.SlugField("URL", max_length=255, unique=True)
    sku = models.CharField("Артикул", max_length=50, unique=True)
    old_price = models.DecimalField(
        "Старая цена", max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)]
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products", verbose_name="Категория")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-price"]
        db_table = "products"

    def __str__(self):
        return self.name
