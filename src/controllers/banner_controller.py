from services.banner_service import create, get_all, get_by_id, update, delete
from schemas.banner_schema import BannerCreateSchema
from fastapi import HTTPException

async def create_banner(data: BannerCreateSchema):
    return await create(data)

async def get_all_banners():
    return await get_all()

async def get_banner(id: int):
    banner = await get_by_id(id)
    if banner is None:
        raise HTTPException(status_code=404, detail='not found')
    return banner

async def update_banner(id: int, data: BannerCreateSchema):
    banner = await update(id, data)
    if banner is None:
        raise HTTPException(status_code=404, detail='not found')
    return banner

async def delete_banner(id: int):
    banner = await delete(id)
    if banner is None:
        raise HTTPException(status_code=404, detail='not found')
    return banner
