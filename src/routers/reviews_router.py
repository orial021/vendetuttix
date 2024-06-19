from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.reviews_schema import ReviewsCreateSchema, ReviewsResponseSchema
from controllers.content_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.auth_router import require_admin

reviews_router = APIRouter()

@reviews_router.get('/all', tags=['Reviews'], response_model=List[ReviewsResponseSchema])
async def all():
    return await get_all_controller()

@reviews_router.get('/show/{id}', tags=['Reviews'], response_model=ReviewsResponseSchema)
async def show(id: int):
    return await get_controller(id)

@reviews_router.post('/create', tags=['Reviews'], response_model=ReviewsResponseSchema)
async def creater(data: ReviewsCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@reviews_router.put('/update/{id}', tags=['Reviews'], response_model=ReviewsResponseSchema)
async def updater(id: int, data: ReviewsCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@reviews_router.delete('/delete/{id}', tags=['Reviews'], response_model=ReviewsResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)