from tortoise import fields
from tortoise.models import Model
from schemas.user_schema import RoleEnum


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField
    password = fields.CharField
    email = fields.CharField
    name = fields.CharField
    rol = fields.CharEnumField(RoleEnum)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(auto_now = True, null = True)

    def __str__(self):
        return self.username
    