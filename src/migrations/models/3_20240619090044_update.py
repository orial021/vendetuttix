from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "username" TYPE VARCHAR(10) USING "username"::VARCHAR(10);
        ALTER TABLE "user" ALTER COLUMN "password" TYPE TEXT USING "password"::TEXT;
        ALTER TABLE "user" ALTER COLUMN "email" TYPE TEXT USING "email"::TEXT;
        ALTER TABLE "user" ALTER COLUMN "name" TYPE TEXT USING "name"::TEXT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "username" TYPE VARCHAR(8) USING "username"::VARCHAR(8);
        ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(12) USING "password"::VARCHAR(12);
        ALTER TABLE "user" ALTER COLUMN "email" TYPE VARCHAR(12) USING "email"::VARCHAR(12);
        ALTER TABLE "user" ALTER COLUMN "name" TYPE VARCHAR(20) USING "name"::VARCHAR(20);"""
