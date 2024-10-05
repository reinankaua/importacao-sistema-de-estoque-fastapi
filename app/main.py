from fastapi import FastAPI
from app.db.conexao import Base, engine
from app.model import *

app = FastAPI()

Base.metadata.create_all(bind=engine)