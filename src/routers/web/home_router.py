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
    print(products)
    return templates.TemplateResponse('home/index.html', {'request': request, 'products': products})

@home_router.get('/productComponent', tags=['Home'])
def index(request: Request):
    return templates.TemplateResponse('components/featured.html', {'request': request})

@home_router.get('/contact', tags=['Home'])
def index(request: Request):
    return templates.TemplateResponse('home/contact.html', {'request': request})

@home_router.get('/departament', tags=['Home'])
def index(request:Request):
    return templates.TemplateResponse('home/departament.html', {'request': request})

@home_router.get('/categoryByDepartament/1', tags=['Home'])
def index(request:Request):
    return templates.TemplateResponse('home/category1.html', {'request': request})

@home_router.get('/categoryByDepartament/2', tags=['Home'])
def index(request:Request):
    return templates.TemplateResponse('home/category2.html', {'request': request})

@home_router.get('/productByCategory/1', tags=['Home'])
def index(request:Request):
    return templates.TemplateResponse('home/products11.html', {'request': request})

@home_router.get('/productByCategory/2', tags=['Home'])
def index(request:Request):
    return templates.TemplateResponse('home/products2.html', {'request': request})