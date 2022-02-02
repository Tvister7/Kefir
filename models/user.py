from tortoise.models import Model
from tortoise.fields import CharField, IntField, DateField, BooleanField, ForeignKeyField


class User(Model):
    id = IntField(pk=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    other_name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    phone = CharField(max_length=20, unique=True)
    birthday = DateField()
    additional_info = CharField(max_length=200)
    is_admin = BooleanField()
    password = CharField(max_length=256)

    city = ForeignKeyField("models.City", related_name="city")

