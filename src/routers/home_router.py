from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, PlainTextResponse
#from app import templates


home_router = APIRouter()


@home_router.get('/', tags=['Home'])
def go_home():
    return RedirectResponse('/home')

@home_router.get('/home', tags=['Home'])
def home():
#def home(request: Request):
    return PlainTextResponse('Esta es la pagina de inicio')
    #return templates.TemplateResponse('base.html', { 'request': request, 'message': 'Welcome'})