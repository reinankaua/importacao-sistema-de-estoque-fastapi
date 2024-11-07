from fastapi import  UploadFile
from services.api_client import APIClient

from app.utils.upload_file import upload_file

class EstoqueProcessor:
    def __init__(self):
        self.api_client = APIClient()
        self.path = "/estoque"

    async def upload_file(self, file: UploadFile):
        return await upload_file(file, self.api_client, self.path)
