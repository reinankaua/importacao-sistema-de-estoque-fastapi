import csv
from fastapi import HTTPException, status, UploadFile
from services.api_client import APIClient


async def upload_file(file: UploadFile, api_client: APIClient, path: str):
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Apenas arquivos CSV são aceitos."
        )

    try:
        contents = await file.read()
        decoded_file = contents.decode("utf-8").splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            api_client.send_data(path, row)

        return {"mensagem": f"Arquivo {file.filename} processado com sucesso"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Falha ao processar o arquivo CSV: {str(e)}"
        )
