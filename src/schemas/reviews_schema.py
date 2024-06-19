from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Reviews(BaseModel):
    id : int
    title : str
    description : str
    qualification : int
    user_id : int
    related_product : Optional[int]
    
    
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Content1',
                'description' : 'description',
                'qualification' : 4,
                'user_id' : 12,
                'related_products' : 85
            }
        }
    }

class ReviewsCreateSchema(BaseModel):
    title : str
    description : str
    qualification : int
    user_id : int
    related_product : Optional[int]
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Content1',
                'description' : 'description',
                'qualification' : 4,
                'user_id' : 12,
                'related_products' : 85
            }
        }
    }
    
    
class ReviewsResponseSchema(ReviewsCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Content1',
                'description' : 'description',
                'qualification' : 4,
                'user_id' : 12,
                'related_products' : 85
            }
        }
    }