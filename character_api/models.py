
from django.db import models


class Character(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'character_api'


class CharacterRole(models.Model):
    label = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'character_role'

