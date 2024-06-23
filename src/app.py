#se inicia usando fastapi dev src/app.py --reload
#se corren migraciones con aerich migrate
#se actualizan migraciones en la BD con aerich upgrade
# auth de usuarios  token: str = Security(oauth2_scheme)
#auth de admins admin_user: User = Depends(require_admin)
#CRUD modelo contact, orden del crud schema, model (__init__.py), service, controller, router (__init__.py)
#modelo para busqueda de una lista por dato especifico reviews/show_by_id

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import routers
from tortoise.contrib.fastapi import register_tortoise
from utils.http_error_handler import HTTPErrorHandler
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from tortoise_conf import TORTOISE_ORM


app = FastAPI()

app.add_middleware(HTTPErrorHandler)
load_dotenv()

origins = [
    "http://localhost:5173",  # Agrega aquí la URL de tu aplicación Svelte
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.title = 'Mi modelo fastAPI'
app.version = '1.0.0'
#app.mount('/assets/styles.css', StaticFiles(directory='../frontend/public/assets/styles.css'), name='static')

register_tortoise(
    app,
    config = TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = False
)

for router, prefix in routers:
    app.include_router(router, prefix=prefix)
    


'''<p>Username: {user.username}</p>
				<p>Password: {user.password}</p>
                <p>Email: {user.email}</p>
                <p>Name : {user.name}</p>
				<p>Rol : {user.rol}</p>
				<p>ID : {user.id}</p>
				<p>Created_at : {user.created_at}</p>
				<p>Updated_at : {user.updated_at}</p>
				<p>deleted_at : {user.deleted_at}</p>'''