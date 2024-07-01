from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "product" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "short_description" VARCHAR(100) NOT NULL,
    "long_description" TEXT,
    "price" DOUBLE PRECISION NOT NULL,
    "promo_price" DOUBLE PRECISION NOT NULL,
    "init_promotional_date" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "end_promotional_date" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "tax" DOUBLE PRECISION NOT NULL,
    "quantity" INT NOT NULL,
    "is_active" BOOL NOT NULL,
    "is_featured" BOOL NOT NULL,
    "is_new" BOOL NOT NULL,
    "category" INT NOT NULL,
    "imagen_url" VARCHAR(50) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "product";"""
