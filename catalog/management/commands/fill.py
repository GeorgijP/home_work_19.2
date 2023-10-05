from catalog.models import Category, Product

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {"name": "Овощи", "description": "Очень полезный продукт!!!"},
            {"name": "Фрукты", "description": "Очень вкусный продукт!!!"},
            {"name": "Ягода", "description": "Очень сладкий продукт!!!"}
        ]
        product_list = [
            {"name": "Малина",
             "description": "Красивая",
             "image": None,
             "category": "Ягода",
             "purchase_price": 600}
        ]

        category_create = []
        for category_item in category_list:
            category_create.append(Category(**category_item))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_create)

        product_create = []
        for product_item in product_list:
            product_create.append(Product(**product_item))

        Product.objects.all().delete()
        Product.objects.bulk_create(product_create)
