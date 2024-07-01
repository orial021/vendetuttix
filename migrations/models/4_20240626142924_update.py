from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "category" DROP COLUMN "departaments_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "category" ADD "departaments_id" VARCHAR(50) NOT NULL;"""
