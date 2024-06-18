from typing import List
from fastapi import APIRouter, Path, Security
from schemas.user_schema import UserCreateSchema, UserResponseSchema
from controllers.user_controller import create_user, get_all_users, get_user, update_user, delete_user
from routers.auth_router import oauth2_scheme

user_router = APIRouter()

@user_router.get('/all', tags=['Banner'], response_model=List[UserResponseSchema])
async def all():
    return await get_all_users()

@user_router.get('/show/{id}', tags=['Banner'], response_model=UserResponseSchema)
async def show(id: int):
    return await get_user(id)

@user_router.post('/create', tags=['Banner'], response_model=UserResponseSchema)
async def creater(data: UserCreateSchema, token: str = Security(oauth2_scheme)):
    return await create_user(data)

@user_router.put('/update/{id}', tags=['Banner'], response_model=UserResponseSchema)
async def updater(id: int, data: UserCreateSchema, token: str = Security(oauth2_scheme)):
    return await update_user(id, data)

@user_router.delete('/delete/{id}', tags=['Banner'], response_model=UserResponseSchema)
async def deleter(id: int, token: str = Security(oauth2_scheme)):
    return await delete_user(id)