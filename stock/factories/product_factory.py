import factory

from constants import DECIMAL_PLACES, MAX_DIGITS


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'stock.Product'

    name = factory.Faker("name")
    quantity = factory.Faker("random_int", min=0, max=15)
    price = factory.Faker("pydecimal", left_digits=MAX_DIGITS, right_digits=DECIMAL_PLACES)
    description = factory.Faker("text")
    image = factory.Faker("file_path", category='image')
