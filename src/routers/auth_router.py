from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import os



auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

secret_key = os.getenv("SECRET_KEY")

users = {
    "jairo":{"username": "jairo", "email": "jairo02193@gmmail.com", "password": "123456"},
    "jairo2":{"username": "jairo2", "email": "jairo021932@gmmail.com", "password": "123456"}
}

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_token(token: str =  Depends(oauth2_scheme)) -> dict:
    try:
        data = jwt.decode(token, secret_key, algorithms= ['HS256'])
        user = users.get(data['username'])
        if user is None:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                                detail = 'Invalid authentication credentials',
                                headers = { 'WWW-Authenticate': 'Bearer'})
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"})

@auth_router.post('/login', tags=['Auth'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user or form_data.password != user['password']:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    token = encode_token({"username": user["username"], "email": user["email"]})
    return { 'access_token': token }

@auth_router.get('/profile', tags=['Auth'])
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user