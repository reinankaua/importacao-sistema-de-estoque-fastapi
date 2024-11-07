import requests

from app.settings.config import Config

class APIClient:
    def __init__(self):
        self.api_url_cliente = Config.FLASK_API_URL

    def send_data(self, url, data):
        try:
            response = requests.post(self.api_url_cliente + url, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao enviar os dados: {e}")

