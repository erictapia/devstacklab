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


# Declaring a request body
# - use a Pydantic model
# - use default for optional attributes
# - a type None will result in a JSON value of null
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/post/items/")
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict

# Declaring path parameters and request body
@app.put("/put/items/{item_id}")
async def put_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# Declaring path parameters, request body, and query
@app.put("/put/query/{item_id}")
async def put_item(item_id: int, item: Item, q: Optional[bool] = None):
    result = {"item_id": item_id, **item.dict()}

    if q:
        result.update({"q": q})

    return result

# Adding additional validation with fastapi.Query
# Validating min/max length and value must match a regex
# - declaring a default value will use a Query object
from fastapi import Query

@app.get("/optional/validation/items")
async def optional_validate_items(q: Optional[str] = Query(None, min_length=1, max_length=10, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results

# Declaring a default value with validation
# - unless query parameter equals the regex, q = "default value"
@app.get("/default/validation/items")
async def optional_validate_items(q: Optional[str] = Query("default value", min_length=1, max_length=10, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    results.update({"q": q})

    return results

# Declaring a required parameter
# - use a Query object with a value of ... on first argument
@app.get("/required/validation/items")
async def required_validate_items(q: str = Query(..., min_length=1, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    results.update({"q": q})

    return results


# Declaring a query parameter that will have a List of strings
# - must use the Query object to define validation rules and default value
# - use Optional for an optional query parameter
# - list can be used instead of List but there will be no validation
from typing import List

@app.get("/list/items")
async def list_items(q: Optional[List[str]] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# Adding additional OpenAPI documentation via a Query object
# - declare a keyword argument name title, this will be seen in the ../redoc page
# - delcare a keyword argument name description, this will be seen on both ../docs and ../redoc
from typing import List

@app.get("/docs/list/items")
async def docs_list_items(
        q: Optional[List[str]] = Query(
            ["Foo", "Bar"],
            title="List of strings",
            description="Query string for the items to search in the database."
        )
):
    query_items = {"q": q}
    return query_items

# Using alias query parameter names which are not valid in Python
@app.get("/invalid/name/")
async def invalid_name(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update(({"q": q}))

    return results


# Deprecating parameters so it shows on the docs
# - use a Query object
# - use keyword argument deprecated=True in the Query object
@app.get("/deprecating/items")
async def deprecating_items(q: Optional[str] = Query(None, alias="item-query", deprecated=True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update(({"q": q}))

    return results


# Validating and metadata on path parameters using fastapi Path
# - use ... as default for required path parameters
# - use Optional[type] for optional
from fastapi import Path

@app.get("/path/validation/{item_id}")
async def path_validation(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query")
):
    results = {"item_id": item_id}

    if q:
        results.update({"q": q})
    
    return results


# Number validation with greater than or equal declaration
# - use ge as condition for the path parameter number
# - the * is a work around for python requiring parameters without a default
#   be declared first. 
# - other validators include: gt, lt, le 
@app.get("/ge/items/{item_id}")
async def ge_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    
    if q:
        results.update({"q": q})
    
    return results


@app.get("/float/items/{item_id}")
async def float_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {
        "item_id": item_id,
        "q": q,
        "size": size
    }
    
    return results


# Mixing path, query, and request body parameter declarations
# - use Item(BaseModel) for defining the body object
# - single json object is passed in request with only the kv pairs of object

@app.put("/mixed/items/{item_id}")
async def mixed_update_item(
        *,
        item_id:int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: Optional[str] = None,
        item: Optional[Item] = None
):
    results = {"item_id": item_id}

    if q:
        results.update({"=q": q})

    if item:
        results.update({"item": item})

    return results


# Multiple body parameters
# - a single json object is passed in request: { obj1, obj2, ..., objn}
# - each body parameter will be of form: obj_name: { kv pairs }
class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/multibody/items/{item_id}")
async def multi_body(item_id: int, item:Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}

    return results


# Declaring a single kv body
#- use a Body
from fastapi import Body

@app.put("/body/items/{item_id}")
async def body_update(item_id: int, item: Item, user: User, importance: int = Body(..., gt=0)):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}

    return results


# Embedding kv on single body parameter
# - add a 'embed=True' argument to the Body

@app.put("/embed/items/{item_id}")
async def embed_update(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}

    return results

# Declaring validation and metadata with Pydantic's Field
from pydantic import Field

@app.put("/field/items/{item_id}")
async def field_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}

    return results


# Declaring model attributes of type Field
class NewItem(BaseModel):
    name: str
    description: Optional[str] = Field (
        None, title="The description of the item", max_length=30
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None

@app.put("/newitem/items/{item_id}")
async def new_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}

    return results
