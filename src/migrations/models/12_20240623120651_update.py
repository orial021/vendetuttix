from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "email" TYPE VARCHAR(30) USING "email"::VARCHAR(30);
        CREATE UNIQUE INDEX "uid_user_email_1b4f1c" ON "user" ("email");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_user_email_1b4f1c";
        ALTER TABLE "user" ALTER COLUMN "email" TYPE TEXT USING "email"::TEXT;"""
