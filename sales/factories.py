from hashlib import sha512

import factory

from constants import STRING_ENCODING


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.User'

    name = factory.Faker("name")
    email = factory.Faker("email")
    is_admin = factory.Faker("boolean")
    password = sha512("password".encode(STRING_ENCODING)).hexdigest()


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
