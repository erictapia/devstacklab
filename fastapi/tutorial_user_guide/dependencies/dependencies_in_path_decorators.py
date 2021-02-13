from fastapi import Depends, FastAPI, Header, HTTPException


app = FastAPI()


# Calling a list of dependencies that do not return a value
# - use a list of fastapi.Depends
# - return values or not, it will not be used in the path operation function
async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")

    return x_key

# - dependencies are evaluated in order, first to fail will dictate response validation message
@app.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
