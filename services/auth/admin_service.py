from typing import Type, TypeVar, Generic
from pydantic import BaseModel
from tortoise.models import Model
from datetime import datetime
from schemas.auth.admin_schema import AdminCreateSchema
from models.admin_model import Admin

T = TypeVar('T', bound=BaseModel)
M = TypeVar('M', bound=Model)

class CRUDService(Generic[T, M]):
    def __init__(self, model: Type[M], schema: Type[T]):
        self.model = model
        self.schema = schema

    '''async def create(self, data: T):
        print("Datos recibidos:", data)
        if 'password' in data.model_dump():
            data.password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        try:
            new_instance = await self.model.create(**data.model_dump())
            print("Nueva instancia creada:", new_instance)
            return new_instance
        except Exception as e:
            print("Error al crear la instancia:", e)
            print("Datos que causaron el error:", data)
            raise e'''
        
        
    async def create(self, data: T):
        return await self.model.create(**data.model_dump())

    async def get_all(self):
        return await self.model.all()

    async def get_by_id(self, id: int):
        return await self.model.get_or_none(id=id)

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

class AdminService(CRUDService[AdminCreateSchema, Admin]):
    pass

admin_service = AdminService(Admin, AdminCreateSchema)
