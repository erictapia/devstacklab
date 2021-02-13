from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header


# All path operations share the following:
# - prefix: /items
# - tags: items
# - dependencies: get_token_header
# - responses: extra data
#
# - use an APIRouter and pass the above once instead of adding it to all
#   the path operations
router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


# /items/
@router.get("/")
async def read_items():
    return fake_items_db

# /items/{item_id}
@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


# /items/{item_id}
@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}}
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException (
            status_code=403, detail="You can only update the item: plumbus"
        )
    
    return {"item_id": item_id, "name": "The great Plumbus"}
