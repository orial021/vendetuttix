from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "about" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "image_url" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
        CREATE TABLE IF NOT EXISTS "banner" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "image_url" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "status" BOOL,
    "click_count" INT,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
        CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "departaments_id" VARCHAR(50) NOT NULL,
    "is_active" BOOL NOT NULL,
    "image_url" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,
    "departament_id" INT NOT NULL REFERENCES "departament" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "contact" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user_id" INT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255),
    "phone" VARCHAR(20),
    "message" TEXT NOT NULL,
    "subject" VARCHAR(100),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
        CREATE TABLE IF NOT EXISTS "content" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "url" VARCHAR(255),
    "image_url" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
        CREATE TABLE IF NOT EXISTS "departament" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "is_active" BOOL NOT NULL,
    "image_url" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
        CREATE TABLE IF NOT EXISTS "error_log" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "error_type" VARCHAR(100) NOT NULL,
    "message" TEXT NOT NULL,
    "traceback" TEXT NOT NULL,
    "url" TEXT NOT NULL,
    "status_code" VARCHAR(15),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
        CREATE TABLE IF NOT EXISTS "product" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "short_description" VARCHAR(100) NOT NULL,
    "long_description" TEXT,
    "price" DOUBLE PRECISION NOT NULL,
    "promo_price" DOUBLE PRECISION NOT NULL,
    "init_promotional_date" TIMESTAMPTZ,
    "end_promotional_date" TIMESTAMPTZ,
    "tax" DOUBLE PRECISION NOT NULL,
    "quantity" INT NOT NULL,
    "is_active" BOOL NOT NULL,
    "is_featured" BOOL NOT NULL,
    "is_new" BOOL NOT NULL,
    "category" VARCHAR(50) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,
    "category_id_id" INT NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "reviews" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "rating" INT NOT NULL,
    "user_id" INT,
    "related_product" INT,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
        CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(30) NOT NULL,
    "password" VARCHAR(60) NOT NULL,
    "email" VARCHAR(30) NOT NULL UNIQUE,
    "name" TEXT NOT NULL,
    "rol" VARCHAR(5) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ
);
COMMENT ON COLUMN "user"."rol" IS 'ADMIN: admin\nUSER: user\nGUEST: guest';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "about";
        DROP TABLE IF EXISTS "banner";
        DROP TABLE IF EXISTS "category";
        DROP TABLE IF EXISTS "contact";
        DROP TABLE IF EXISTS "content";
        DROP TABLE IF EXISTS "departament";
        DROP TABLE IF EXISTS "error_log";
        DROP TABLE IF EXISTS "product";
        DROP TABLE IF EXISTS "reviews";
        DROP TABLE IF EXISTS "user";"""
