import asyncio
from datetime import date
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
    print(f"wait {timeout}s than respond {date.today()}")
    await asyncio.sleep(timeout)
    return {f"message: wait {timeout}s than respond {date.today()}"}


@app.get("/t2")
async def root():
    print(f"wait 15s than respond {date.today()}")
    await asyncio.sleep(15)
    return {f"message: wait 25s than respond {date.today()}"}


@app.get("/d")
async def root():
    return {f"message: respond direct: {date.today()}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
