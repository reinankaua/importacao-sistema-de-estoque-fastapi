from fastapi import FastAPI

from .cliente_router import router as files

def init_routes(app: FastAPI):
    app.include_router(files)