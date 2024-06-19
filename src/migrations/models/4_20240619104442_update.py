from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "errorlog" ADD "status_code" VARCHAR(15);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "errorlog" DROP COLUMN "status_code";"""
