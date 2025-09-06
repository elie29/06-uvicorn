import asyncio
from datetime import datetime
from random import randint
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(
    title="Uvicorn Server",
    version="1.0",
    description="A simple API server",
)

# Serve favicon from root folder
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/t1/{user}")
async def root(user: str):
    timeout = randint(5, 30)
    print(f"{user} wait {timeout}s than respond {datetime.now()}")
    await asyncio.sleep(timeout)
    print(f"{user} finished {datetime.now()}")
    return {f"message: wait {timeout}s than respond {datetime.now()}"}


@app.get("/t2/{user}")
async def root(user: str):
    print(f"{user} wait 15s than respond {datetime.now()}")
    await asyncio.sleep(15)
    print(f"{user} finished {datetime.now()}")
    return {f"message: wait 25s than respond {datetime.now()}"}


@app.get("/d")
async def root():
    return {f"message: respond direct: {datetime.now()}"}

@app.get("/b")
def root():
    i = 0
    while(i<1000000):
        i += 1
    return {f"message: respond blocked: {datetime.now()}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, workers=4)
