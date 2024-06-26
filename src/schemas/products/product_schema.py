from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    id: int
    name: str
    short_description: str
    long_description: str
    price: float
    promo_price: float
    init_promotional_date: datetime | None = None
    end_promotional_date: datetime | None = None
    tax: float | None = None
    quantity: int
    is_active: bool
    is_featured: bool
    is_new: bool
    category: int
    imagen_url: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'name':'string',
                'short_description':'string',
                'long_description':'string',
                'price':'string',
                'promo_price':'string',
                'init_promotional_date':'string',
                'end_promotional_date':'string',
                'tax':'string',
                'quantity':1,
                'is_active':'True',
                'is_featured':'True',
                'is_new':'True',
                'category':1,
                'imagen_url':'string',
            }
        }
    }

class ProductCreateSchema(BaseModel):
    name: str
    short_description: str
    long_description: str
    price: float
    promo_price: float
    init_promotional_date: datetime | None = None
    end_promotional_date: datetime | None = None
    tax: float | None = None
    quantity: int
    is_active: bool
    is_featured: bool
    is_new: bool
    category: int
    imagen_url: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'name':'string',
                'short_description':'string',
                'long_description':'string',
                'price':'string',
                'promo_price':'string',
                'init_promotional_date':'string',
                'end_promotional_date':'string',
                'tax':'string',
                'quantity':1,
                'is_active':'True',
                'is_featured':'True',
                'is_new':'True',
                'category':1,
                'imagen_url':'string',
            }
        }
    }

class ProductResponseSchema(ProductCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'name':'string',
                'short_description':'string',
                'long_description':'string',
                'price':'string',
                'promo_price':'string',
                'init_promotional_date':'string',
                'end_promotional_date':'string',
                'tax':'string',
                'quantity':1,
                'is_active':'True',
                'is_featured':'True',
                'is_new':'True',
                'category_id':'string',
                'imagen_url':'string',
            }
        }
    }

