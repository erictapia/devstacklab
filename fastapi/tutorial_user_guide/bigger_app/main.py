from fastapi import Depends, FastAPI

from bigger_app.dependencies import get_query_token, get_token_header
from bigger_app.internal import admin
from bigger_app.routers import items, users


# FastAPI with global dependencies
app = FastAPI(dependencies=[Depends(get_query_token)])


# include submodule routers to the FastAPI application
app.include_router(users.router)
app.include_router(items.router)

# include routers with custom arguments
# - useful when a router submodule is shared and cannot directly include
#   prefix paths, tags, dependencies, and custom responses
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_query_token)],
    responses={418: {"description": "I'm a teapot"}}
)

# Adding a path operation directly to the FastAPI application
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
