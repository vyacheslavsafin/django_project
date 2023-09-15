from catalog.models import Category, Product

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_list = [
            {'name': 'Смартфоны и гаджеты', 'description': 'Мобильные телефоны, планшеты'},
            {'name': 'Ноутбуки и компьютеры', 'description': 'Стационарные и мобильные ПК'},
            {'name': 'Телевизоры и цифровое ТВ', 'description': 'Телевизоры, приставки, спутниковые тарелки'},
            {'name': 'Аудиотехника', 'description': 'Портативные колонки, наушники, саундбары'},
        ]

        categories_to_create = []
        for category_item in category_list:
            categories_to_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_to_create)
