from typing import Optional

from fastapi import Cookie, Depends, FastAPI


app = FastAPI()


# Dependencies with sub-dependencies
# - sub-dependencies can be multi-level deep


# - 2nd level dependency
def query_extractor(q: Optional[str] = None):
    return q


# - first level dependency
def query_or_cookie_extractor(
        q: str = Depends(query_extractor),
        last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query

    return q

# - Dependency return flow: query_extractor -> query_or_cookie_extractor -> /items
# - if dependencies is declared multiple times for the same path operation
#   FastAPI will know to call the sub-dependency only once per request.
#   It will cache the return value and pass it to all the dependants unless
#   use_cache=False is passed as a argument.
@app.get("/items")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}
