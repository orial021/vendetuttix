from routers.home_router import home_router
from routers.users_router import user_router
from routers.auth_router import auth_router
from routers.banner_router import banner_router

routers = [
    (home_router, '/home'),
    (user_router, '/user'),
    (auth_router, '/auth'),
    (banner_router, '/banner')
    
] 
