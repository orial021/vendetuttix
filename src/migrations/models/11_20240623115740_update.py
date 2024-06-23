from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "exam" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user_id" INT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255),
    "phone" VARCHAR(20),
    "message" TEXT NOT NULL,
    "on_top" BOOL NOT NULL,
    "classss" VARCHAR(5) NOT NULL,
    "subject" VARCHAR(100),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "exam"."classss" IS 'ADMIN: admin\nUSER: user\nGUEST: guest';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "exam";"""
