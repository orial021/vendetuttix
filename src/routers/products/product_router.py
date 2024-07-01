from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from models.user_model import User
from schemas.products.product_schema import ProductCreateSchema, ProductResponseSchema
from controllers.products.product_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller, get_by_category, get_featured
from routers.user.auth_router import require_admin
from templates import templates

product_router = APIRouter()

@product_router.get('/all', tags=['Product'], response_model=List[ProductResponseSchema])
async def all(offset: int = 0, limit: int = 12, order_by: str = "name"):
    return await get_all_controller(offset, limit, order_by)

@product_router.get('/show/{id}', tags=['Product'], response_model=ProductResponseSchema)
async def show(id: int):
    return await get_controller(id)

@product_router.get('/detail/{product_id}', tags=['Product'], response_model=ProductResponseSchema)
async def product_detail(request: Request, product_id: int):
    product = await get_controller(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return templates.TemplateResponse('product/product_detail.html', {'request': request, 'product': product})

@product_router.get('/showByCategory/{categoryId}', tags=['Product'], name="show_by_category", response_model=List[ProductResponseSchema])
async def show_by_id(categoryId : int, offset: int = 0, limit: int = 12, order_by: str = "name"):
    return await get_by_category(categoryId, offset, limit, order_by)

@product_router.get('/showFeatured/{is_featured}', tags=['Product'], name="show_featured_products", response_model=List[ProductResponseSchema])
async def show_featured(is_featured: bool = True, offset: int = 0, limit: int = 4, order_by: str = "updated_at"):
    return await get_featured(is_featured, offset, limit, order_by)

@product_router.post('/create', tags=['Product'], response_model=ProductResponseSchema)
async def creater(data: ProductCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@product_router.put('/update/{id}', tags=['Product'], response_model=ProductResponseSchema)
async def updater(id: int, data: ProductCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@product_router.delete('/delete/{id}', tags=['Product'], response_model=ProductResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)