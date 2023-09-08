from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories = [
            {'name': "Грибы", 'description': "из леса"},
            {'name': "Фрукты", 'description': "из магазина"}
        ]

        category_to_fill = []
        for category in categories:
            category_to_fill.append(Category(**category))

        Category.objects.bulk_create(category_to_fill)