from typing import List
from fastapi import APIRouter, Path, Security
from schemas.banner_schema import BannerCreateSchema, BannerResponseSchema
from controllers.banner_controller import create_banner, get_all_banners, get_banner, update_banner, delete_banner
from routers.auth_router import oauth2_scheme

banner_router = APIRouter()

@banner_router.get('/all', tags=['Banner'], response_model=List[BannerResponseSchema])
async def all_banners():
    return await get_all_banners()

@banner_router.get('/show/{id}', tags=['Banner'], response_model=BannerResponseSchema)
async def show_banner(id: int = Path(..., description='The ID of the banner to get')):
    return await get_banner(id)

@banner_router.post('/create', tags=['Banner'], response_model=BannerResponseSchema)
async def creater_banner(data: BannerCreateSchema, token: str = Security(oauth2_scheme)):
    return await create_banner(data)

@banner_router.put('/update/{id}', tags=['Banner'], response_model=BannerResponseSchema)
async def updater_banner(id: int, data: BannerCreateSchema, token: str = Security(oauth2_scheme)):
    return await update_banner(id, data)

@banner_router.delete('/delete/{id}', tags=['Banner'], response_model=BannerResponseSchema)
async def deleter_banner(id: int = Path(..., description='The ID of the banner to delete'), token: str = Security(oauth2_scheme)):
    return await delete_banner(id)