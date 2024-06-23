from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Exam(BaseModel):
    id: int
    user_id: int
    name: str
    email: str
    phone: str
    message: str
    on_top: bool
    classss: str
    subject: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'user_id':1,
                'name':'string',
                'email':'string',
                'phone':'string',
                'message':'string',
                'on_top':'True',
                'classss':'Other',
                'subject':'string',
            }
        }
    }

class ExamCreateSchema(BaseModel):
    user_id: int
    name: str
    email: str
    phone: str
    message: str
    on_top: bool
    classss: str
    subject: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'user_id':1,
                'name':'string',
                'email':'string',
                'phone':'string',
                'message':'string',
                'on_top':'True',
                'classss':'Other',
                'subject':'string',
            }
        }
    }

class ExamResponseSchema(ExamCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'user_id':1,
                'name':'string',
                'email':'string',
                'phone':'string',
                'message':'string',
                'on_top':'True',
                'classss':'Other',
                'subject':'string',
            }
        }
    }

