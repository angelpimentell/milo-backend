import factory

from constants import DECIMAL_PLACES
from sales.factories import CartFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'stock.Product'

    name = factory.Faker("name")
    quantity = factory.Faker("random_int", min=0, max=15)
    price = factory.Faker("pydecimal", right_digits=DECIMAL_PLACES)


class ProductCartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'stock.ProductCart'

    product = factory.SubFactory(ProductFactory)
    cart = factory.SubFactory(CartFactory)


class ProductInvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'stock.ProductInvoice'

    product = factory.SubFactory(ProductFactory)
    cart = factory.SubFactory(CartFactory)
    price = factory.Faker("pydecimal", right_digits=DECIMAL_PLACES)
