import asyncio
from fastapi import FastAPI
import uvicorn

## App definition
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain runnable interfaces",
)


@app.get("/")
async def root():
    asyncio.sleep(5)
    return {"message: wait 5s than respond"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
