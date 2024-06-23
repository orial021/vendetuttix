from routers.web.home_router import home_router
from routers.user.users_router import user_router
from routers.user.auth_router import auth_router
from routers.web.banner_router import banner_router
from routers.web.content_router import content_router
from routers.web.reviews_router import reviews_router
from routers.web.contact_router import contact_router
from routers.web.about_router import about_router

routers = [
    (home_router, '/home'),
    (user_router, '/user'),
    (auth_router, '/auth'),
    (banner_router, '/banner'),
    (content_router, '/content'),
    (reviews_router, '/reviews'),
    (contact_router, '/contact'),
    (about_router, '/about'),
    
] 
