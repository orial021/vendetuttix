import httpx
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, RedirectResponse, PlainTextResponse
from templates import templates


home_router = APIRouter()


@home_router.get('/', tags=['Home'])
def go_home():
    return RedirectResponse('/home')

@home_router.get('/home', tags=['Home'], response_class=FileResponse)
def home():
    return "<p>Hello Jairo</p>"

@home_router.get('/page', tags=['Home'])
async def index(request: Request):
    async with httpx.AsyncClient() as client:
        url = request.url_for("show_featured_products", is_featured=True)
        response = await client.get(str(url), params={"offset": 0, "limit": 4, "order_by": "updated_at"})
        products = response.json()
    if not isinstance(products, list):
        raise ValueError("Expected a list of products")
    return templates.TemplateResponse('home/index.html', {'request': request, 'products': products})

@home_router.get('/productByCategory/{categoryId}', tags=['Home'])
async def index(categoryId: int, request:Request):
    async with httpx.AsyncClient() as client:
        url = request.url_for("show_by_category", categoryId=categoryId)
        response = await client.get(str(url), params={"categoryId": int, "offset": 0, "limit": 4, "order_by": "name"})
        products = response.json()
    if not isinstance(products, list):
        raise ValueError("Expected a list of products")
    return templates.TemplateResponse('home/products.html', {'request': request, 'products': products})

@home_router.get('/categoryByDepartament/{departamentId}', tags=['Home'])
async def index(departamentId: int, request:Request):
    async with httpx.AsyncClient() as client:
        url = request.url_for("show_category_by_departament", departamentId=departamentId)
        response = await client.get(str(url), params={"departamentId": int})
        categories = response.json()
    if not isinstance(categories, list):
        raise ValueError("Expected a list of products")
    return templates.TemplateResponse('home/categories.html', {'request': request, 'categories': categories})

@home_router.get('/categoryAll', tags=['Home'])
async def index(request:Request):
    async with httpx.AsyncClient() as client:
        url = request.url_for("category_all")
        response = await client.get(str(url))
        categories = response.json()
    if not isinstance(categories, list):
        raise ValueError("Expected a list of products")
    return templates.TemplateResponse('home/categoryAll.html', {'request': request, 'categories': categories})

@home_router.get('/productAll', tags=['Home'])
async def index(request:Request):
    async with httpx.AsyncClient() as client:
        url = request.url_for("product_all")
        response = await client.get(str(url))
        products = response.json()
    if not isinstance(products, list):
        raise ValueError("Expected a list of products")
    return templates.TemplateResponse('home/productAll.html', {'request': request, 'products': products})


@home_router.get('/productComponent', tags=['Home'])
def index(request: Request):
    return templates.TemplateResponse('components/featured.html', {'request': request})

@home_router.get('/contact', tags=['Home'])
def index(request: Request):
    return templates.TemplateResponse('home/contact.html', {'request': request})

@home_router.get('/departament', tags=['Home'])
def index(request:Request):
    return templates.TemplateResponse('home/departament.html', {'request': request})






