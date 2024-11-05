from fastapi import FastAPI

from .cliente_router import router as cliente_router
from .produto_router import router as produto_router
from .estoque_router import router as estoque_router

def init_routes(app: FastAPI):
    app.include_router(cliente_router)
    app.include_router(produto_router)
    app.include_router(estoque_router)
