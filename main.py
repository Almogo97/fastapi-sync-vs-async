import asyncio
from contextlib import asynccontextmanager

import aiohttp
import requests
from fastapi import FastAPI

url = "http://localhost:8000/sleep"


@asynccontextmanager
async def lifespan(app: FastAPI):
    global http_client
    http_client = aiohttp.ClientSession()
    yield
    await http_client.close()


app = FastAPI(lifespan=lifespan)


@app.get("/requests_async")
async def requests_async(seconds: float):
    response = requests.get(f"{url}?seconds={seconds}")
    return response.json()


@app.get("/requests_sync")
def requests_sync(seconds: float):
    response = requests.get(f"{url}?seconds={seconds}")
    return response.json()


@app.get("/requests_to_thread_async")
async def requests_to_thread_async(seconds: float):
    response = await asyncio.to_thread(requests.get, f"{url}?seconds={seconds}")
    return response.json()


@app.get("/aiohttp_async")
async def aiohttp_async(seconds: float):
    async with http_client.get(f"{url}?seconds={seconds}") as response:
        return await response.json()
