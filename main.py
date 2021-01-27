from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# AUTO OPENAPI DOCUMENTATION
# localhost:8000/docs
# localhost:8000/redoc
# localhost:8000/openapi.json