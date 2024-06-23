from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "error_log" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "error_type" VARCHAR(100) NOT NULL,
    "message" TEXT NOT NULL,
    "traceback" TEXT NOT NULL,
    "url" TEXT NOT NULL,
    "status_code" VARCHAR(15),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
        CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(30) NOT NULL,
    "hashed_password" TEXT NOT NULL,
    "email" VARCHAR(30) NOT NULL UNIQUE,
    "name" TEXT NOT NULL,
    "rol" VARCHAR(5) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "user"."rol" IS 'ADMIN: admin\nUSER: user\nGUEST: guest';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "error_log";
        DROP TABLE IF EXISTS "user";"""
