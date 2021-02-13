from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Optional


app = FastAPI()


# Declaring response model for path operations: get, post, put, delete, etc.
# - response model is a parameter of the decorator method
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = list()


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


# Don't do this in production
@app.post("/user", response_model=UserIn)
async def create_user(user: UserIn):
    return user


# Using an input and output model
# - in must have all required out attributes
# - out will filter out attributes not declared in out
# - Missing attribute will cause a 500 response code
class UserIn2(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/inout/user", response_model=UserOut)
async def inout_create_user(user: UserIn):
    return user


# Response model with default values
# - use "response_model_exclude_unset=True" to omit unset attributes
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# Response model includes a subset of the Model
# - use "response_model_include=" set, list, or tuple with attribute name's
# - use "response_model_exclude=" set, list, or tuple with attribute name's
# - the OpenAPI docs will use the complete Model regardless of what is included or excluded
@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"}
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]
