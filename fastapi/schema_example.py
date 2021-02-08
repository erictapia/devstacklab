from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()

# Declaring OpenAPI example data via a Pydantic model using Config and schema_extra
# - example info will be added as-is to the example/JSON Schema
class Item(BaseModel):
    name: str
    descriptioni: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "Item description",
                "price": 35.4,
                "tax": 3.2
            }
        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}

    return results


# Adding examples to Field arguments
class FieldItem(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="Item description")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

@app.put("/field/items/{item_id}")
async def field_update_item(item_id: int, item: FieldItem):
    results = {"item_id": item_id, "item": item}

    return results


# Adding examples to a Body type
class BodyItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/body/items/{item_id}")
async def body_update_item(
        item_id: int,
        item: BodyItem = Body(
            ...,
            example={
                "name": "Foo",
                "description": "A description",
                "price": 35.4,
                "tax": 3.2
            }
        )
):
    results = {"item_id": item_id, "item": item}

    return results
