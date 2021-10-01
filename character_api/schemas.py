from ninja import ModelSchema, Schema
from character_api.models import Character, CharacterRole

"""
TODO: why can't I use the cute ModelSchema method?
class CharacterIn(ModelSchema):
    class Meta:
        model = Character
        exclude = ["id"]



class CharacterOut(ModelSchema):
    class Meta:
        model = Character
        fields = "__all__"
        required = "__all__"
"""


class CharacterRoleIn(Schema):
    label: str


class CharacterRoleOut(Schema):
    label: str
    id: int