from tortoise import fields
from tortoise.models import Model

from schemas.user.user_schema import RoleEnum


class Exam(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=20, null=True)
    message = fields.TextField()
    on_top = fields.BooleanField()
    classss = fields.CharEnumField(RoleEnum)
    subject = fields.CharField(max_length=100, null=True)
    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(auto_now = True, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        table = "exam"