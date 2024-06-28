from services.products.product_service import product_service
from schemas.products.product_schema import ProductCreateSchema
from fastapi import HTTPException

async def create_controller(data: ProductCreateSchema):
    return await product_service.create(data)

async def get_all_controller(offset = 0, limit = 10, order_by = "name"):
    return await product_service.get_all(offset, limit, order_by)

async def get_controller(id: int):
    product = await product_service.get_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product

async def get_by_category(category_id : int, offset = 0, limit = 10, order_by = "name"):
    product = await product_service.get_by_category(category_id, offset, limit, order_by)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product

async def get_featured(is_featured, offset = 0, limit = 4, order_by = "updated_at"):
    product = await product_service.get_featured(is_featured, offset, limit, order_by)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product

async def update_controller(id: int, data: ProductCreateSchema):
    product = await product_service.update(id, data)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product

async def delete_controller(id: int):
    product = await product_service.delete(id)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product