from fastapi import APIRouter, UploadFile, File

from domain.estoque_processor import EstoqueProcessor

router = APIRouter()

@router.post("/importar-estoque/")
async def upload_file(file: UploadFile = File(...)):
    return await EstoqueProcessor().upload_file(file)