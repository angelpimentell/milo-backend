import factory
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sales.User'

    name = factory.Faker("name")
    email = factory.Faker("email")
    is_superuser = factory.Faker("boolean")
    password = make_password("password")
