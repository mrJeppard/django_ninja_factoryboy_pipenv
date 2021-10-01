from character_api.models import CharacterRole
import factory


class CharacterRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CharacterRole

    label = factory.Sequence(lambda n: 'label-%s' % n)



