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
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})

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