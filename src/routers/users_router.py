from typing import List
from fastapi import APIRouter, Path, Security
from schemas.user_schema import UserCreateSchema, UserResponseSchema
from controllers.user_controller import user_controller
from routers.auth_router import oauth2_scheme

user_router = APIRouter()

@user_router.get('/all', tags=['User'], response_model=List[UserResponseSchema])
async def all():
    return await user_controller.get_all_users()

@user_router.get('/show/{id}', tags=['User'], response_model=UserResponseSchema)
async def show(id: int):
    return await user_controller.get_user(id)

@user_router.post('/create', tags=['User'], response_model=UserResponseSchema)
async def creater(data: UserCreateSchema):
    return await user_controller.create_user(data)

@user_router.put('/update/{id}', tags=['User'], response_model=UserResponseSchema)
async def updater(id: int, data: UserCreateSchema, token: str = Security(oauth2_scheme)):
    return await user_controller.update_user(id, data)

@user_router.delete('/delete/{id}', tags=['User'], response_model=UserResponseSchema)
async def deleter(id: int, token: str = Security(oauth2_scheme)):
    return await user_controller.delete_user(id)