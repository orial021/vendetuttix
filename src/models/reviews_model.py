from tortoise import fields
from tortoise.models import Model


class Reviews(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    qualification = fields.IntField(ge = 1, le = 5)
    user_id = fields.IntField()
    related_product = fields.IntField(null = True)
    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(auto_now = True, null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        table = "reviews"