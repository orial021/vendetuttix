from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.exam_schema import ExamCreateSchema, ExamResponseSchema
from controllers.exam_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

exam_router = APIRouter()

@exam_router.get('/all', tags=['Exam'], response_model=List[ExamResponseSchema])
async def all():
    return await get_all_controller()

@exam_router.get('/show/{id}', tags=['Exam'], response_model=ExamResponseSchema)
async def show(id: int):
    return await get_controller(id)

@exam_router.post('/create', tags=['Exam'], response_model=ExamResponseSchema)
async def creater(data: ExamCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@exam_router.put('/update/{id}', tags=['Exam'], response_model=ExamResponseSchema)
async def updater(id: int, data: ExamCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@exam_router.delete('/delete/{id}', tags=['Exam'], response_model=ExamResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)