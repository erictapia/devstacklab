from typing import Optional

from fastapi import Depends, FastAPI


app = FastAPI()


# Dependencies should be a "callable" which in Python is anything that Python can "call" like a function
# - A class is callable Class(...) which means it can be used as a dependency
# - fastapi will analyze the parameters of the callable
# - fastapi will process parameters the same way as the parameters for a path operation function, including
#   sub-dependencies
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# - fastapi will call the CommonQueryParams, create an instance, and pass the instance as an argument in
#   the path operation function
@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = dict()

    if commons.q:
        response.update({"q": commons.q})

    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})

    return response


# Shortcut when a dependency is a Class
# - use var: Type = Depends()
# - the above will mean the same as var: Type = Depends(Type)
@app.get("/shortcut/items/")
async def shortcut_read_items(commons: CommonQueryParams = Depends()):
    response = dict()

    if commons.q:
        response.update({"q": commons.q})

    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})

    return response
