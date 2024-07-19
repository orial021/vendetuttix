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

from routers import routers
from tortoise.contrib.fastapi import register_tortoise
from utils.http_error_handler import HTTPErrorHandler
from dotenv import load_dotenv
from tortoise_conf import TORTOISE_ORM

from fastapi_admin.app import app as admin_app, FastAPIAdmin
from fastapi_admin.providers.login import UsernamePasswordProvider
from models.admin_model import Admin
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


admin_app = FastAPIAdmin(
    admin_path='/panel',
    logo_url="https://example.com/logo.png",
    login_logo_url="https://example.com/login_logo.png",
    providers=[
        UsernamePasswordProvider(
            admin_model=Admin,
            login_logo_url="https://example.com/login_logo.png",
        )
    ],
)
app.mount('/panel', admin_app)

register_tortoise(
    app,
    config = TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = True
)

@app.on_event("startup")
async def startup():
    await Tortoise.init(config=TORTOISE_ORM)
    await admin_app._register_providers()


for router, prefix in routers:
    app.include_router(router, prefix=prefix)

    
@app.get('/', tags=['Home'])
def go_home():
    return RedirectResponse('/home/page')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
