import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a

    return {"hello world": b}

# Run uvicorn from script to allow debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
