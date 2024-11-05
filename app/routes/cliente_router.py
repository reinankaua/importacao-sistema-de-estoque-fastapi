from fastapi import APIRouter, UploadFile, File

from domain.cliente_processor import ClienteProcessor

router = APIRouter()

@router.post("/importar-clientes/")
async def upload_file(file: UploadFile = File(...)):
    return await ClienteProcessor().upload_file(file)