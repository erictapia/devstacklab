from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


app = FastAPI()

# Returning client side error HTTP response codes
# - use fastapi.HTTPException
# - the detail argument can be anything that can be converted to a dict and is handled by fastapi
items = { "foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item": items[item_id]}


# Adding custom headers
# - use the headers key argument
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"}
        )

    return {"item": items[item_id]}


# Using custom exception handlers such as exceptions from a 3rd party package
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# Custom exception handler
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something."}
    )


# Raises exception when name equals yolo
@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)

    return {"unicorn_name": name}


# Override the default exception handlers
# Fastapi internally has a RequestValidationError exception that is raised when data validation fails.
# It also has a default exception handler but it can be override
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


# handles custom raised exception
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail) + " <-- starlette exception",status_code=exc.status_code)


# Handles validation exceptions
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc) + " <-- validation exception", status_code=400)


@app.get("/exc/items/{item_id}")
async def exc_read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")

    return {"item_id": item_id}
