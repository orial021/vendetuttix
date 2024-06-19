from services.reviews_service import reviews_service
from schemas.reviews_schema import ReviewsCreateSchema
from fastapi import HTTPException

async def create_controller(data: ReviewsCreateSchema):
    return await reviews_service.create(data)

async def get_all_controller():
    return await reviews_service.get_all()

async def get_controller(id: int):
    reviews = await reviews_service.get_by_id(id)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews

async def update_controller(id: int, data: ReviewsCreateSchema):
    reviews = await reviews_service.update(id, data)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews

async def delete_controller(id: int):
    reviews = await reviews_service.delete(id)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews
