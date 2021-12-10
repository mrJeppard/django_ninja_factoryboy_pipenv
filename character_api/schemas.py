from ninja import Schema


class CharacterRoleIn(Schema):
    label: str


class CharacterRoleOut(Schema):
    label: str
    id: int
