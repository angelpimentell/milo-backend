import factory

from constants import DECIMAL_PLACES
from sales.factories import CartFactory
from . import ProductFactory


class ProductInvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'stock.ProductInvoice'

    product = factory.SubFactory(ProductFactory)
    cart = factory.SubFactory(CartFactory)
    price = factory.Faker("pydecimal", right_digits=DECIMAL_PLACES)
