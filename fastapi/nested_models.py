from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Dict, List, Optional, Set

app = FastAPI()

# Declaring a set with a string type parameter
# - any duplicates will be converted to a set of unique items
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}

    return results

# Defining a submodel
# - HttpUrl will validate URL syntax
# - image is an optional Image thus nesting model
class Image(BaseModel):
    url: HttpUrl
    name: str


class ImageItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[List[Image]] = None


@app.put("/image/items/{item_id}")
async def image_update_item(item_id: int, item: ImageItem):
    results = {"item_id": item_id, "item": item}

    return results


# Deeply nested models
class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[ImageItem]

@app.post("/offers")
async def create_offer(offer: Offer):
    return offer

# Defining a dict that is limited to integer keys and float values.
# - json only supports keys as a string
# - Pydantic will convert the string to an integer
@app.post("/index-weights")
async def create_index_weights(weights: Dict[int, float]):
    return weights
