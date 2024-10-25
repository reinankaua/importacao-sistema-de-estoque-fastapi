from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, utils
import csv

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/importar-clientes/")
async def importar_clientes(file: UploadFile = File(...), db: Session = SessionLocal()):
    # Valida e processa o CSV de clientes
    try:
        utils.importar_clientes_csv(file, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao importar clientes: {str(e)}")
    return {"message": "Clientes importados com sucesso"}

# Repita esse processo para produtos e estoque
