from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Departament(BaseModel):
    id: int
    title: str
    description: str
    departament_id: Optional[str] = None
    is_active: bool
    image_url: str
    link: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'title':'string',
                'description':'string',
                'is_active':'True',
                'image_url':'string',
                'link':'string'
            }
        }
    }

class DepartamentCreateSchema(BaseModel):
    title: str
    description: str
    departament_id: Optional[str] = None
    is_active: bool
    image_url: str
    link: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'title':'string',
                'description':'string',
                'is_active':'True',
                'image_url':'string',
                'link':'string'
            }
        }
    }

class DepartamentResponseSchema(DepartamentCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'title':'string',
                'description':'string',
                'is_active':'True',
                'image_url':'string',
                'link':'string'
            }
        }
    }

