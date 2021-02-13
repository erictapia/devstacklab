from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


# Declaring HTTP status code
# - use status_code in decorator
# - OpenAPI docs will include the status code
@app.post("/items", status_code=201)
async def create_item(name: str):
    return {"name": name}


# Same as above but using fastapi.status constants for http response code
# and IDE for autocomplete.  It may reduce errors.
@app.post("/status/items", status_code=status.HTTP_201_CREATED)
async def status_create_item(name: str):
    return {"name": name}