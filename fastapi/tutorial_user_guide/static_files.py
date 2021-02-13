from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()


# Mounting: means adding a complete independent application in a specific path
# that then takes care of handling all the sub-paths
# - OpenAPI and docs will not include anything from the mounted application
# - "/static" refers to a sub-path (sub-application) will be mounted on
# - any path that starts with "/static" will be handled by the sub-path mount
# - name="static" is a name that can be used internally by FastAPI
app.mount("/static", StaticFiles(directory="static"), name="static")
