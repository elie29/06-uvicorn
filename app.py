import asyncio
from random import randint
from syslog import syslog
from fastapi import FastAPI
import uvicorn

## App definition
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain runnable interfaces",
)


@app.get("/t1")
async def root():
    timeout = randint(5, 30)
    print(f"wait {timeout}s than respond")
    await asyncio.sleep(timeout)
    return {f"message: wait {timeout}s than respond"}


@app.get("/t2")
async def root():
    await asyncio.sleep(15)
    return {"message: wait 25s than respond"}


@app.get("/d")
async def root():
    return {"message: respond direct!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
