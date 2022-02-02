from tortoise.models import Model
from tortoise.fields import CharField, IntField


class City(Model):
    id = IntField(pk=True)
    name = CharField(unique=True)
