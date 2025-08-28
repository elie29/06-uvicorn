import asyncio
from datetime import datetime
from random import randint
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
    print(f"wait {timeout}s than respond {datetime.now()}")
    await asyncio.sleep(timeout)
    print(f"Finished {datetime.now()}")
    return {f"message: wait {timeout}s than respond {datetime.now()}"}


@app.get("/t2")
async def root():
    print(f"wait 15s than respond {datetime.now()}")
    await asyncio.sleep(15)
    print(f"Finished {datetime.now()}")
    return {f"message: wait 25s than respond {datetime.now()}"}


@app.get("/d")
async def root():
    return {f"message: respond direct: {datetime.now()}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
