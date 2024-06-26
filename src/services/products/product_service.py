from typing import Type, TypeVar, Generic
from pydantic import BaseModel
from tortoise.models import Model
from datetime import datetime
from schemas.products.product_schema import ProductCreateSchema
from models.product_model import Product

T = TypeVar('T', bound=BaseModel)
M = TypeVar('M', bound=Model)

class CRUDService(Generic[T, M]):
    def __init__(self, model: Type[M], schema: Type[T]):
        self.model = model
        self.schema = schema

    async def create(self, data: T):
        return await self.model.create(**data.model_dump())

    async def get_all(self):
        return await self.model.all()

    async def get_by_id(self, id: int):
        return await self.model.get_or_none(id=id)
    
    async def get_by_user(self, user_id: int):
        return await self.model.filter(user_id=user_id).all()

    async def update(self, id: int, data: T):
        instance = await self.get_by_id(id)
        if instance:
            await instance.update_from_dict(data.model_dump()).save()
            return instance
        return None

    async def delete(self, id: int):
        instance = await self.get_by_id(id)
        if instance:
            instance.deleted_at = datetime.now()
            await instance.save()
            return instance
        return None

class ProductService(CRUDService[ProductCreateSchema, Product]):
    pass

product_service = ProductService(Product, ProductCreateSchema)
