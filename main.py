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
