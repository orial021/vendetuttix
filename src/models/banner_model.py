from tortoise import fields
from tortoise.models import Model


class Banner(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    image_url = fields.TextField()
    content = fields.TextField()
    status = fields.BooleanField(null = True)
    click_count = fields.IntField(null = True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(auto_now = True, null = True)

    def __str__(self):
        return self.title
    
