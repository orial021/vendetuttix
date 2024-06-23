from routers.home_router import home_router
from routers.users_router import user_router
from routers.auth_router import auth_router
from routers.banner_router import banner_router
from routers.content_router import content_router
from routers.reviews_router import reviews_router
from routers.contact_router import contact_router
from routers.exam_router import exam_router

routers = [
    (home_router, '/home'),
    (user_router, '/user'),
    (auth_router, '/auth'),
    (banner_router, '/banner'),
    (content_router, '/content'),
    (reviews_router, '/reviews'),
    (contact_router, '/contact'),
    (exam_router, '/exam'),
    
] 
