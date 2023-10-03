from catalog.models import Category, Product

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {"name_category": "Овощи", "description_category": "Очень полезный продукт!!!"},
            {"name_category": "Фрукты", "description_category": "Очень вкусный продукт!!!"},
            {"name_category": "Ягода", "description_category": "Очень сладкий продукт!!!"}
        ]
        product_list = [
            {"name_product": "Малина",
             "description_product": "Красивая",
             "image_product": None,
             "category_product": "Ягода",
             "purchase_price_product": 600}
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
