# Pydantic models

from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


# class Config is configuration for the Pydantic model
# - orm_mode = True configures Pydantic to also try reading value
#   using ORM accessors, data.id instead of only data["id"]
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = list()

    class Config:
        orm_mode = True
