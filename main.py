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


