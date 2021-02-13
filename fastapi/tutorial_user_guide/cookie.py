from fastapi import Cookie, FastAPI
from typing import Optional


app = FastAPI()

# Declaring Cookie parameter
# - use fastapi Cookie

@app.get("/items")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}
