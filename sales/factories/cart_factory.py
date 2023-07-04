import factory

from ..factories.user_factory import UserFactory


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.Cart'

    user = factory.SubFactory(UserFactory)
    done = factory.Faker("boolean")
