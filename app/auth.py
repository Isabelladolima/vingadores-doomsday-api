from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "usuarios/login")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha_digitada: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_digitada, senha_hash)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
TOKEN_EXPIRA_MINUTOS = 60

def criar_token(dados: dict) -> str:
    dados_para_codificar = dados.copy()
    expira_em = datetime.utcnow() + timedelta(minutes = TOKEN_EXPIRA_MINUTOS)
    dados_para_codificar.update({"exp": expira_em})
    token = jwt.encode(dados_para_codificar, SECRET_KEY, algorithm = ALGORITHM)
    return token

def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    excecao_credenciais = HTTPException(
        status_code = 401,
        detail = "Não foi possível validar as credenciais",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise excecao_credenciais
        return username
    except JWTError:
        raise excecao_credenciais