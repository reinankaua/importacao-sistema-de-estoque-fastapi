from fastapi import APIRouter, UploadFile, File

from domain.produto_processor import ProdutoProcessor

router = APIRouter()

@router.post("/importar-produtos/")
async def upload_file(file: UploadFile = File(...)):
    return await ProdutoProcessor().upload_file(file)