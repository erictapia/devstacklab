from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()


# Authenticating username/password with OAuth2
# - OpenAPI docs will have an "Authorize" button that can be used to
#   authenticate and test
#
# Password Flow via a Bearer token:
# - user enters username/password in the frontend
# - frontend transmit credentials to an endpoint in the API path operation
# - API checks username/password, and responds with a "token"
# - the frontend temporarily stores the token
# - user explores other areas in the frontend
# - the frontend sends a header "Authorization" with a value that is the
#   concatenation of "Bearer " and the token value
# - each endpoint the user wishes to view has to be authentication via the
#   "Authorization" header

# - tokenURL is to the URL used to authenticate, in this example it will be
#   a relative URL, ./token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# - the dependency will return a string and assigned to the token variable
# - fastapi will know this dependency will require a "security scheme" and
#   document it in the OpenAPI docs
# - if the Authorization header or the Bearer token is missing, fastapi will
#   respond with a 401 status code
#
# THIS CODE DOES NOT VALIDATE TOKEN
@app.get("/items")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
