from services.user_service import user_service
from schemas.user_schema import UserCreateSchema
from fastapi import HTTPException

async def create_user(data: UserCreateSchema):
    return await user_service.create(data)

async def get_all_users():
    return await user_service.get_all()

async def get_user(id: int):
    user = await user_service.get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail='not found')
    return user

async def update_user(id: int, data: UserCreateSchema):
    user = await user_service.update(id, data)
    if user is None:
        raise HTTPException(status_code=404, detail='not found')
    return user

async def delete_user(id: int):
    user = await user_service.delete(id)
    if user is None:
        raise HTTPException(status_code=404, detail='not found')
    return user
