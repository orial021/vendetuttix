# service/banner_service.py
from models.banner_model import Banner as This
from schemas.banner_schema import BannerCreateSchema
from datetime import datetime

async def create(data: BannerCreateSchema):
    return await This.create(**data.model_dump())

async def get_all():
    return await This.all()

async def get_by_id(id: int):
    return await This.get_or_none(id=id)

async def update(id: int, data: BannerCreateSchema):
    banner = await get_by_id(id)
    if banner:
        await banner.update_from_dict(data.model_dump()).save()
        return banner
    return None

async def delete(id: int):
    banner = await get_by_id(id)
    if banner:
        banner.deleted_at = datetime.now()
        await banner.save()
        return banner
    return None
