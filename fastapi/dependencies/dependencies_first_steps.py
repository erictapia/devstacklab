# Dependency injection - is a way for dependencies to be injected into FastAPI
#
# Usefulness:
# - shared logic(code repetition)
# - shared database connections
# - enforce security, authentication, role requirements, etc.
# - ...

from typing import Optional


from fastapi import Depends, FastAPI


app = FastAPI()


# Shared code used for injecting, aka dependency
async def common_parameters(
        q: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


# Path operations injected with path operation function parameters
# - use fastapi.Depends to inject dependencies
# - OpenAPI docs will document query parameters
# - FastAPI will add parameters, validations, etc. to the path operations
# - flow: Depends(function) -> path operation function( injecting Depend return parameters)
@app.get("/items")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
