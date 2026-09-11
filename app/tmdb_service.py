import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def buscar_filme_por_nome(nome_filme: str):
    url = f"{TMDB_BASE_URL}/search/movie"
    parametros = {
        "api_key": TMDB_API_KEY,
        "query": nome_filme,
        "language": "pt-BR",
    }
    reposta = requests.get(url, params = parametros)
    return reposta.json()

def buscar_elenco(tmdb_id: int):
    url = f"{TMDB_BASE_URL}/movie/{tmdb_id}/credits"
    parametros = {
        "api_key": TMDB_API_KEY,
        "language": "pt-BR",
    }
    resposta = requests.get(url, params = parametros)
    return resposta.json()