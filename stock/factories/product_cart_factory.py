import factory

from . import ProductFactory
from sales.factories import CartFactory


class ProductCartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'stock.ProductCart'

    product = factory.SubFactory(ProductFactory)
    cart = factory.SubFactory(CartFactory)
