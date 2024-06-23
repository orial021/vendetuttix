from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse, PlainTextResponse
#from app import templates


home_router = APIRouter()


@home_router.get('/', tags=['Home'])
def go_home():
    return RedirectResponse('/home')

@home_router.get('/home', tags=['Home'], response_class=FileResponse)
def home():
    return 'frontend/public/index.html'