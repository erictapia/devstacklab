from fastapi import FastAPI

# AUTO OPENAPI DOCUMENTATION
# localhost:8000/docs
# localhost:8000/redoc
# localhost:8000/openapi.json

app = FastAPI()

# FastAPI will handle requests with
# - the path "/"
# - using a "get" operation
@app.get("/")
async def root():
    return {"message": "Hello World"}


# The path can be used to declare parameters such as "{item_id}" in the
#   path: "/items/{item_id}"
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# The type can be declared using Python type annotations
# - if parameter is not of same type, auto generates json with an error msg.
@app.get("/items_int/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# The order of endpoint declarations matter.
# - declare specific endpoint first
# - delcare generic endpoint after
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Using enum to predefine a path parameter
# - declare path parameter with a type annotation of the enum class
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}


# Including a parameter with a str value that is a path
# - This uses a Starlette option, path, that matches a string path
# - OpenAPI does not support paths but FastAPI will provide documentation
#     except it will not be a path and instead a string type.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return{"file_path": file_path}


# parameters that are not part of a path can be interpreted as "query" parameters
# as long as it follows these rules:
# - query parameters follow after a ?
# - query parameters are separated by an & character

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/query")
async def read_query(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# Query parameters can be declare to be optional.
# Using the typing.Optional class, the editor can help find errors in the code
from typing import Optional

@app.get("/optional_query/{item_id}")
async def read_opt_query(item_id: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q} if q else {"item_id": item_id}

# Declaring a query bool type
@app.get("/bool_conversion/{item_id}")
async def read_bool_query(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


# Declaring multiple path parameters and query parameters
# - declared order does not matter

@app.get("/multiple/users/{user_id}/items/{item_id}")
async def read_multiple_path(
        # Path parameters
        user_id: int, item_id: str,

        # Query parameters
        q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


# Declaring required query parameters
# - add additional arguments to the definition
# - do not declare any default
@app.get("/required/items/{item_id}")
async def read_required(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}
