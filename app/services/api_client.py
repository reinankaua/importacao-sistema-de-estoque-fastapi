import requests

from settings.config import Config

class APIClient:
    def __init__(self):
        self.api_url_cliente = Config.FLASK_API_URL_CLIENTE
        self.api_url_produto = Config.FLASK_API_URL_PRODUTO
        self.api_url_estoque = Config.FLASK_API_URL_ESTOQUE

    def send_data_cliente(self, data):
        try:
            response = requests.post(self.api_url_cliente, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao enviar dados de cliente: {e}")

    def send_data_produto(self, data):
        try:
            response = requests.post(self.api_url_produto, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao enviar dados de produto: {e}")

    def send_data_estoque(self, data):
        try:
            response = requests.post(self.api_url_estoque, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao enviar dados de estoque: {e}")