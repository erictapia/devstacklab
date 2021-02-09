from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Union


app = FastAPI()


# Using different models based on in/out/db
# - input could use plaintext password
# - output could omit password
# - db could use hashed password

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None


def fake_password_hasher(raw_password: str):
    return f"supersecret {raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")

    return user_in_db


# - Input will have a password
# - In DB will have a hashed password
# - Out, response, will not have a password. Its not defined in model.
@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)

    return user_saved


# Reducing duplication code between models by using a UserBase model
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn2(UserBase):
    password: str


class UserOut2(UserBase):
    pass


class UserInDB2(UserBase):
    hashed_password: str


def fake_password_hasher2(raw_password: str):
    return f"supersecret {raw_password}"


def fake_save_user2(user_in: UserIn2):
    hashed_password = fake_password_hasher2(user_in.password)
    user_in_db = UserInDB2(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")

    return user_in_db


# - Input will have a password
# - In DB will have a hashed password
# - Out, response, will not have a password. Its not defined in model.
@app.post("/user2", response_model=UserOut2)
async def create_user(user_in: UserIn2):
    user_saved = fake_save_user2(user_in)

    return user_saved


# Response can be any of two types using typing.Union
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


# - use Union[model1,model2, ..., modeln]
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


# List of models
class Item(BaseModel):
    name: str
    description: str


items_list = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items_list", response_model=List[Item])
async def read_items():
    return items_list
