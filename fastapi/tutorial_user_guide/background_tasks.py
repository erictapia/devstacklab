from typing import Optional

from fastapi import BackgroundTasks, Depends, FastAPI


app = FastAPI()


# Sending a response and then run a process in the background
# - background task can be async def or def
def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)


# - task arguments will be the function name, and any arguments required by function
@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")

    return {"message": "Notification sent in the background"}


# Using BackgroundTasks with dependencies
def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)


@app.post("/depends/send-notification/{email}")
async def depends_send_notification(
        email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)

    return {"message": "Message sent"}
