import os 
import requests
from dotenv import load_dotenv

load_dotenv()

COMICVINE_API_KEY = os.getenv("COMICVINE_API_KEY")
COMICVINE_BASE_URL = "https://comicvine.gamespot.com/api"

def buscar_personagem(nome_personagem: str):
    url = f"{COMICVINE_BASE_URL}/search/"
    parametros = {
        "api_key": COMICVINE_API_KEY,
        "query": nome_personagem,
        "field_list": "id,name,real_name,deck,image",
        "format": "json",
    }
    headers = {
        "User-Agent": "VingadoresDoomsdayAPI/1.0",
    }
    resposta = requests.get(url, params=parametros, headers=headers)
    return resposta.json()

def buscar_aparicoes(personagem_id: int):
    url = f"{COMICVINE_BASE_URL}/character/4005-{personagem_id}/"
    parametros = {
        "api_key": COMICVINE_API_KEY,
        "field_list": "id,name,issue_credits",
        "format": "json",
    }
    headers = {
        "User-Agent": "VingadoresDoomsdayAPI/1.0",
    }
    resposta = requests.get(url, params=parametros, headers= headers)
    return resposta.json()