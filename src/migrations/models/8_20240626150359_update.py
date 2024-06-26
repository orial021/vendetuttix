from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "product";
        DROP TABLE IF EXISTS "category";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ;"""
