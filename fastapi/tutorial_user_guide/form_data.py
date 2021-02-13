from fastapi import FastAPI, Form


app = FastAPI()


# Receiving form fields instead of JSON
# - request should use "application/x-www-form-urlencoded"
# - alternatively, when including files, use "multipart/form-data"
# - must use Form for declaring form bodies instead of JSON bodies
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}
