import factory

from ..factories.user_factory import UserFactory


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.Invoice'

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("name")
    paid = factory.Faker("boolean")
