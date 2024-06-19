from tortoise import fields
from tortoise.models import Model
from schemas.user_schema import RoleEnum


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=10)
    password = fields.TextField(max_length=15)
    email = fields.TextField(max_length=30)
    name = fields.TextField(max_length=20)
    rol = fields.CharEnumField(RoleEnum)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(auto_now = True, null = True)

    def __str__(self):
        return self.username
    