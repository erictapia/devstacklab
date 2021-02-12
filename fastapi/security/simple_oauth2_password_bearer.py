from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


app = FastAPI()


# OAuth2 specs on password flow
# - client must send a username and password as form data
# - security permissions will be sent in the "scope" form field where
#   all specify security permission are separated by spaces


def fake_hash_password(password: str):
    return f"fakehashed{password}"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)

    return user

# OAuth2 spec states additional headers WWW-Authenticate with value Bearer will
# be returned on a 401 unauthorized response
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    print(f"\nget current user:\n{token}\n{user}")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    print(f"\ncurrent active user\n{current_user}")
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user

# OAuth2 spec says the return has to be JSON with an access_token, and a
# token_type.
# - using x-www-form-urlencoded pass the "username" and "password"
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    print(f"\ntoken\n{user_dict}")
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

# User must autheticate via /token path to get the access_token
# - in the headers, set the "Authorization" to "Bearer Token"
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    print(f"\nusers me\n{current_user}")
    return current_user
