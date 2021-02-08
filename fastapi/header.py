from fastapi import FastAPI, Header
from typing import List, Optional


app = FastAPI()


# Defining header parameters
# - use fastapi Header otherwise it will be interpreted as a query parameter
# - Header will convert a '-' into a '_' so it is usable in Python
# - HTTP headers are case-insensitive
@app.get("/items")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}


# Request with duplicate headers
# - headers will be received as a list
@app.get("/duplicate/header/items")
async def duplicate_read_items(x_token: Optional[List[str]]= Header(None)):
    return {"X-Token values": x_token}
