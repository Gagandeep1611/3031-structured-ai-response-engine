from fastapi import FastAPI

from app.aws_help.routers import router

app = FastAPI()

app.include_router(router)
