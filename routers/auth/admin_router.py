from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.auth.admin_schema import AdminCreateSchema, AdminResponseSchema
from controllers.auth.admin_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

admin_router = APIRouter()

@admin_router.get('/all', tags=['Admin'], response_model=List[AdminResponseSchema])
async def all():
    return await get_all_controller()

@admin_router.get('/show/{id}', tags=['Admin'], response_model=AdminResponseSchema)
async def show(id: int):
    return await get_controller(id)

@admin_router.post('/create', tags=['Admin'], response_model=AdminResponseSchema)
async def creater(data: AdminCreateSchema):
    return await create_controller(data)

@admin_router.put('/update/{id}', tags=['Admin'], response_model=AdminResponseSchema)
async def updater(id: int, data: AdminCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@admin_router.delete('/delete/{id}', tags=['Admin'], response_model=AdminResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)