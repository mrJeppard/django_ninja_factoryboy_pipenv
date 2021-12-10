from typing import List
from ninja import Router
from character_api import models
from character_api.schemas import CharacterRoleOut, CharacterRoleIn
from ninja.security import django_auth


router = Router()


@router.post(
    '/role',
    response=CharacterRoleOut,
    auth=django_auth,
    url_name="character_role"
)
def post_character_role(
    request,
    character_in: CharacterRoleIn
):
    """Doc strings are displayed in swagger documentation."""
    return models.CharacterRole.objects.create(**character_in.dict())


@router.get(
    '/role',
    response=List[CharacterRoleOut],
    auth=django_auth,
    url_name="character_role"
)
def get_character_role(request):
    return models.CharacterRole.objects.all()


@router.get(
    '/role/{role_id}',
    response=CharacterRoleOut,
    auth=django_auth,
    url_name="character_role"
)
def get_character_role(request, role_id: int):
    return models.CharacterRole.objects.get(pk=role_id)


