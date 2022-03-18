from fastapi import FastAPI
from bot_api.settings.dev import init_db
from tortoise import run_async
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    run_async(init_db())
    uvicorn.run(app, host="0.0.0.0", port=8000)

