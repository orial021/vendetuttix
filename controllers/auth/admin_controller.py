from services.auth.admin_service import admin_service
from schemas.auth.admin_schema import AdminCreateSchema
from fastapi import HTTPException

async def create_controller(data: AdminCreateSchema):
    return await admin_service.create(data)

async def get_all_controller():
    return await admin_service.get_all()

async def get_controller(id: int):
    admin = await admin_service.get_by_id(id)
    if admin is None:
        raise HTTPException(status_code=404, detail='not found')
    return admin

async def update_controller(id: int, data: AdminCreateSchema):
    admin = await admin_service.update(id, data)
    if admin is None:
        raise HTTPException(status_code=404, detail='not found')
    return admin

async def delete_controller(id: int):
    admin = await admin_service.delete(id)
    if admin is None:
        raise HTTPException(status_code=404, detail='not found')
    return admin