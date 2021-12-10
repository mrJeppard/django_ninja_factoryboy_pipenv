from typing import List
from ninja import Router
from character_api import models
from character_api.schemas import CharacterRoleOut, CharacterRoleIn
from ninja.security import django_auth


role_router = Router()


@role_router.post(
    '/',
    response=CharacterRoleOut,
    auth=django_auth,
    url_name="character_role",
    tags=["Role"]

)
def post_character_role(
    request,
    character_in: CharacterRoleIn,
):
    """Doc strings are displayed in swagger documentation."""
    return models.Role.objects.create(**character_in.dict())


@role_router.get(
    '/',
    response=List[CharacterRoleOut],
    auth=django_auth,
    url_name="character_role",
    tags=["Role"]
)
def get_character_roles(request):
    return models.Role.objects.all()


@role_router.get(
    '/{role_id}',
    response=CharacterRoleOut,
    auth=django_auth,
    url_name="character_role",
    tags=["Role"]
)
def get_character_role(request, role_id: int):
    return models.Role.objects.get(pk=role_id)


