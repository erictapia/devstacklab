from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()


# Uploading files via fastapi.File
# - request uses form-data
# - use fastapi.File
# - will be stored in memory
# - will work well for small files
@app.post("/files")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# Uploading big files
# - use typ fastapi.UploadFile
# - UploadFile type will store in memory up to max size limit then store to disk
# - you can get metadata
# - UploadFile has async methods: write, read, seek, close.  Require await
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }


# Multiple file uploads via typing.List
@app.post("/multiple/files")
async def multiple_create_file(files: List[bytes] = File(...)):
    return {"file_size": [len(file) for file in files]}


@app.post("/multiple/uploadfiles")
async def multiple_create_upload_file(files: List[UploadFile] = File(...)):
    return {
        "filenames": [file.filename for file in files]
    }


# Testing form helper
@app.get("/")
async def main():
    content = """
        <body>
            <form action="/multiple/files" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
            <form action="/multiple/uploadfiles" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
             </form>
        </body>
    """

    return HTMLResponse(content=content)
