import csv
from fastapi import HTTPException, status, UploadFile
from services.api_client import APIClient


class EstoqueProcessor:
    def __init__(self):
        self.api_client = APIClient()

    async def upload_file(self, file: UploadFile):

        if file.filename.endswith('.csv'):
            try:
                contents = await file.read()
                decoded_file = contents.decode("utf-8").splitlines()

                csv_reader = csv.DictReader(decoded_file)
                for row in csv_reader:
                    self.api_client.send_data_estoque(row)

                return {"mensagem": f"Arquivo {file.filename} processado com sucesso"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail=f"Falha ao processar a arquivo CSV: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Apenas arquivos CSV são aceitos.")