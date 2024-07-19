#se inicia usando fastapi dev src/app.py --reload
#se corren migraciones con aerich migrate
#se actualizan migraciones en la BD con aerich upgrade
# auth de usuarios  token: str = Security(oauth2_scheme)
#auth de admins admin_user: User = Depends(require_admin)
#CRUD modelo contact, orden del crud schema, model (__init__.py), service, controller, router (__init__.py)
#modelo para busqueda de una lista por dato especifico reviews/show_by_id
#tailwind npx tailwindcss -i .\static\css\app.css -o .\static\css\app.css --watch
#entorno virtual venv\Scripts\Activate.ps1 

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from admin_config import init_admin
from routers import routers
from tortoise.contrib.fastapi import register_tortoise
from utils.http_error_handler import HTTPErrorHandler
from dotenv import load_dotenv
from tortoise_conf import TORTOISE_ORM

from tortoise import Tortoise


app = FastAPI()

app.add_middleware(HTTPErrorHandler)
load_dotenv()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.title = 'Mi modelo fastAPI'
app.version = '1.0.0'

register_tortoise(
    app,
    config = TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = True
)

@app.on_event("startup")
async def startup():
    await init_admin(app)

for router, prefix in routers:
    app.include_router(router, prefix=prefix)

    
@app.get('/', tags=['Home'])
def go_home():
    return RedirectResponse('/home/page')


