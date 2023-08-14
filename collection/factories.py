import factory
from .models import GameCollection
from usersapp.factories import UserFactory



class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameCollection
    
    name = factory.Sequence(
        lambda n: f'Test collection {n}'
    )
    author = factory.SubFactory(UserFactory)
