import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/sleep")
async def sleep(seconds: float):
    await asyncio.sleep(seconds)
    return {"message": f"Slept for {seconds}"}
