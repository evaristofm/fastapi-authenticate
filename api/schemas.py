from tortoise.contrib.pydantic import pydantic_model_creator
from .models import User, Item
from pydantic import BaseModel

class ItemIn(BaseModel):
    name: str

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

Item_Pydantic = pydantic_model_creator(Item, name='Item')
ItemIn_Pydantic = pydantic_model_creator(Item, name='ItemIn', exclude_readonly=True)
