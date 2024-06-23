from services.web.reviews_service import reviews_service
from schemas.web.contact_schema import ContactCreateSchema
from fastapi import HTTPException

async def create_controller(data: ContactCreateSchema):
    return await reviews_service.create(data)

async def get_all_controller():
    return await reviews_service.get_all()

async def get_controller(id: int):
    contact = await reviews_service.get_by_id(id)
    if contact is None:
        raise HTTPException(status_code=404, detail='not found')
    return contact

async def update_controller(id: int, data: ContactCreateSchema):
    contact = await reviews_service.update(id, data)
    if contact is None:
        raise HTTPException(status_code=404, detail='not found')
    return contact

async def delete_controller(id: int):
    contact = await reviews_service.delete(id)
    if contact is None:
        raise HTTPException(status_code=404, detail='not found')
    return contact