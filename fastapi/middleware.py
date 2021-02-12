import time

from fastapi import FastAPI, Request


app = FastAPI()


# Middleware is a function that works with every request prior to processing
# with a path operation function or before processing a response return
# - it can run a pre-processor for each request
# - after the pre-processor, it process request as it normally would
# - same for the response, pre-processor and then normal processing
# - yield dependencies and background tasks run after the pre-processors
# - use the @app.middleware decorator

# Middleware function receives
# - request
# - call_next function that receives the request
# - response can then be modified


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response

# Middleware will automatically add the X-Process-Time in the response headers.
@app.get("/")
async def root():
    return {"test": "root"}