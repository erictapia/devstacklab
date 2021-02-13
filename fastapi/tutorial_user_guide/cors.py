from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# CORS (Cross-Origin Resource Sharing" refers to frontend running in a different "origin" than the backend
# Origin is a combination of protocol, domain, and port
# - backend must have a list of "allowed origins" so browsers allow frontend javascript to be ran in a CORS
#   environment
# - use * (a wildcard) to allow all but limited to certain types, it excludes everything that involves credentials
# - it's best to specify explicitly the allowed origins
#
# - use fastapi.middelware.cors.CORSMiddleware
# - use a list of allowed origins
# - add it as a middleware to the FastAPI application


origins = [
    "http://localhost:8080",
    "http://localhost"
]

# By default, CORSMiddleware is restrictive
# - use arguments to explicitly enable:
#   - allow_origins: a list of allowed origins
#   - allow_origin_regex: a regex string to match allowed origins
#   - allow_methods: methods allows in CORS requests, default is ["GET"]
#   - allow_headers: list of supported CORS requests headers, default is []
#   - allow_credentials: allows COR request cookies, default is False
#   - expose_headers: any response headers accessible to the browsers, default is []
#   - max_age: seconds browser should cache CORS responses, default is 600
# - responds only to:
#   - OPTIONS request that include an Origin and Access-Control-Request-Method headers
#     CORS middleware will intercept, respond with CORS headers, and either a 200 or 400 response
#   - any request with an Origin header
#     CORS middleware will pass request through as normal and include appropriate CORS headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
