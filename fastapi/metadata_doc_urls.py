from fastapi import FastAPI


# Metadata for tags
# - a list of dictionaries
# - each tag requires a dictionary and contains:
#   - name (required): a string with same name as tag
#   - description: a string with a short description, can be markdown
#   - externalDocs: a dict describing external documentation
#     - description: a string with a short description
#     - url (required): a string with URL of the external documentation
#
# - list order is how tags are listed in the OpenAPI docs
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    }
]


# Customizing metadata configurations in the FastAPI application
# - title: API's title/name in the OpenAPI and automatic API docs UIs
# - description
# - version
# - openapi_url: can be used to change the default: /openapi.json or disable by = None
# - docs_url
# - redoc_url
app = FastAPI(
    title="My Super Project",
    description="This is a very fancy project",
    version="2.5.0",
    openapi_tags=tags_metadata,
    docs_url="/api",
    redoc_url=None,
    #openapi_url=None #"/api/v1/openapi.json"
)


@app.get("/items", tags=["items"])
async def read_items():
    return [{"name": "Foo"}]


@app.get("/users", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]
