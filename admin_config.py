from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Model
from models import Admin
from aioredis import from_url

async def init_admin(app):
    redis = await from_url("redis://localhost")
    await admin_app.configure(
        redis=redis,
        logo_url="https://example.com/logo.png",
        providers=[
            UsernamePasswordProvider(admin_model=Admin)
        ],
    )

    class AdminResource(Model):
        label = "Admin"
        model = Admin
        icon = "fas fa-user"
        fields = [
            "id",
            "username",
            "email",
            "is_active",
            "created_at",
            "updated_at",
        ]

    admin_app.register(AdminResource)
    app.mount("/admin", admin_app)
