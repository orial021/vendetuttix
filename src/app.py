#se inicia usando fastapi dev src/app.py --reload
#se corren migraciones con aerich migrate
#se actualizan migraciones en la BD con aerich upgrade
# auth de usuarios  token: str = Security(oauth2_scheme)
#auth de admins admin_user: User = Depends(require_admin)

from fastapi import FastAPI
from routers import routers
from tortoise.contrib.fastapi import register_tortoise
from utils.http_error_handler import HTTPErrorHandler
from dotenv import load_dotenv
from tortoise_conf import TORTOISE_ORM

#from utils.dependencies import init_app


app = FastAPI()


app.add_middleware(HTTPErrorHandler)
load_dotenv()

#templates = init_app(app)
app.title = 'Mi modelo fastAPI'
app.version = '1.0.0'


register_tortoise(
    app,
    config = TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = False
)

for router, prefix in routers:
    app.include_router(router, prefix=prefix)
    
