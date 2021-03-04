import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise
from passlib.hash import bcrypt
from typing import List

from .auth import JWT_SECRET, authenticate_user, get_current_user
from .schemas import (
    User_Pydantic, UserIn_Pydantic,
    Item_Pydantic, ItemIn_Pydantic, ItemIn
)
from .models import User, Item

app = FastAPI()


@app.get('/')
async def main():
    return {"Hello": "World"}

@app.post('/token')
async def generate_token(data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid username or password')
    
    user_obj = await User_Pydantic.from_tortoise_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return {'access_token': token, 'token_type': 'bearer'}

@app.post('/users', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = User(username=user.username, password_hash=bcrypt.hash(user.password_hash))
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(user_obj)

@app.get('/users/me', response_model=User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user

@app.post('/items', response_model=Item_Pydantic)
async def create_item(item: ItemIn, user: User_Pydantic = Depends(get_current_user)):
    item_obj = await Item.create(name=item.name, user_id=user.id)
    item_obj.save()
    return await Item_Pydantic.from_tortoise_orm(item_obj)

@app.get('/items', response_model=List[Item_Pydantic])
async def get_items(skip: int = 0, limit: int = 20):
    return await Item_Pydantic.from_queryset(Item.filter().offset(skip).limit(limit).all())

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['api.models']},
    generate_schemas=True,
    add_exception_handlers=True
)


