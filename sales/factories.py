from django.contrib.auth.hashers import make_password

import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.User'

    name = factory.Faker("name")
    email = factory.Faker("email")
    is_superuser = factory.Faker("boolean")
    password = make_password("password")


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.Cart'

    user = factory.SubFactory(UserFactory)
    done = factory.Faker("boolean")


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.Invoice'

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("name")
    paid = factory.Faker("boolean")
