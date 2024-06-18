from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(8) NOT NULL,
    "password" VARCHAR(12) NOT NULL,
    "email" VARCHAR(12) NOT NULL,
    "name" VARCHAR(20) NOT NULL,
    "rol" VARCHAR(5) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "user"."rol" IS 'ADMIN: admin\nUSER: user\nGUEST: guest';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""
