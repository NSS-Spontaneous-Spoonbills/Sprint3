from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from website.models import Customer
from website.models import Order
from website.models import Payment_Option
from website.models import Payment_Type
from website.models import Product
from website.models import Product_Type
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Allows command line integration for faker_factory.py"""

    def handle(self, *args, **options):
        """Utilizes Faker to create mock data for the database, The arguments for most seeds are ([Model], [Number of records])."""

        # the number argument is the total num of rows you want created

        # seeder.add_entity(User, 12)
        seeder.add_entity(Customer, 120)
        # seeder.add_entity(Payment_Type, 120)
        seeder.add_entity(Payment_Option, 120, {
            'account_number': lambda x: random.randint(11111, 99999)})
        seeder.add_entity(Order, 120)
        # seeder.add_entity(Product_Type, 12)
        seeder.add_entity(
            Product, 120, {'title': lambda x: seeder.faker.catch_phrase()})

        inserted_pks = seeder.execute()
