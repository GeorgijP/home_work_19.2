from catalog.models import Category, Product

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {"name_category": "Овощи", "description_category": "Очень полезный продукт!"},
            {"name_category": "Фрукты", "description_category": "Очень вкусный продукт!"}
        ]

        category_create = []
        for category_item in category_list:
            category_create.append(Category(**category_item))

        Category.objects.bulk_create(category_create)
