from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавление тестовых товаров'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(
            self.style.WARNING('Старые данные удалены')
        )

        call_command('loaddata', 'catalog_fixture.json')

        self.stdout.write(
            self.style.SUCCESS('Тестовые данные успешно загружены')
        )