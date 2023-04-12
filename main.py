from fastapi import FastAPI
from devopslib.randomfruits import fruit
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API.  Call /search or /wiki"}


@app.get("/fruit/random")
async def fuit_random():
    return {"fruit": fruit()}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")