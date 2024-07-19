from tortoise import fields
from tortoise.models import Model
import uuid


class Admin(Model):
    id = fields.IntField(pk=True, max_length=36)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null = True)

    def __str__(self):
        return self.username
    
    class Meta:
        table = "admin"