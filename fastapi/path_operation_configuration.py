from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional, Set


app = FastAPI()


# Passing parameters to path operation decorator's
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()

# - use response_model for model used as response and on OpenAPI docs
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item


# - adding tags to path operation causes endpoint to be listed under the
#   tag name
# - decorator without a tag is shown under "default" tag
@app.post("/tag/items", response_model=Item, tags=["items"])
async def tag_create_item(item: Item):
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


# Adding a summary
# - use summary to display text after the endpoint path of the OpenAPI docs
# - use description to display text inside the expanded endpoint of the OpenAPI docs
@app.post(
    "/summary/items",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax, and tags"
)
async def summary_create_tag(item: Item):
    return item


# Using docstring as an alternative to the decorator description key
@app.post("/docstring/items/", response_model=Item, summary="Create an item")
async def docstring_create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# Using a response description
# - use response_description
# - the text will be shown on the 200 response code section
@app.post(
    "/response/items/",
    response_model=Item,
    summary="Create an item",
    response_description="The created item",
)
async def response_create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# Declaring a deprecate path operation
# - use deprecated = true
# - OpenAPI docs will displayed it greyed out, strikethrough, and a deprecated warning
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
