from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()


# Convert a model to a compatible JSON (dict or list)
fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None

# - use fastapi.encoders.jsonable_encoder to convert to a Python data structure
#   compatible with JSON
@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(fake_db)
