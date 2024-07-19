from enum import Enum
import uuid
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Admin(BaseModel):
    id: int
    username: str
    password: str
    is_active: Optional[bool] = True


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':'1',
                'username':'string',
                'password':'string',
                'is_active': True,
            }
        }
    }

class AdminCreateSchema(BaseModel):
    username: str
    password: str
    is_active: Optional[bool] = True


    model_config = { 
       'json_schema_extra':{
            'example':{
                'username':'string',
                'password':'string',
                'is_active': True,
            }
        }
    }

class AdminResponseSchema(AdminCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':'1',
                'username':'string',
                'password':'string',
                'is_active': True,
            }
        }
    }

