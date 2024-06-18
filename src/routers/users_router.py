from typing import Annotated

from fastapi import APIRouter, Depends

user_router = APIRouter()

@user_router.get('/sellers', tags=['Users'])
def get_sellers( start_date: str, end_date: str ):
    return f"Usuarios creados entre {start_date} and {end_date}"

def common_params(start_date: str, end_date: str):
    return { "start_date": start_date, "end_date": end_date }

@user_router.get('/customers', tags=['Users'])
def get_customers(commons: dict = Depends(common_params)):
    return f"CLientes creados entre {commons['start_date']} and {commons['end_date']}"

@user_router.get('/users', tags=['Users'])
def get_users( commons: Annotated[dict, Depends(common_params)]):
    return f"Usuarios creados entre {commons['start_date']} and {commons['end_date']}"

CommonDep = Annotated[dict, Depends(common_params)]

@user_router.get('/buyers', tags=['Users'])
def get_buyers( commons: CommonDep ):
    return f"Usuarios creados entre {commons['start_date']} and {commons['end_date']}"

class CommonDeps:
    def __init__(self, start_date: str, end_date: str) -> None:
        self.star_date = start_date
        self.end_date = end_date
        
@user_router.get('/uzers', tags=['Users'])
def get_uzers( commons: CommonDeps = Depends() ):
    return f"Uzuarios creados entre {commons.star_date} and {commons.end_date}"