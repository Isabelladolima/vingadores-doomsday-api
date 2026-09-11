from sqlalchemy import Column, Integer, String
from app.database import Base

class FilmeDB(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    titulo_original = Column(String)
    data_lancamento = Column(String)
    sinopse = Column(String) 

class ElencoDB(Base):
    __tablename__ = "elenco"

    id = Column(Integer, primary_key = True, index = True)
    pessoa_id = Column(Integer)
    nome = Column(String)
    personagem = Column(String)
    foto_path = Column(String)
    ordem = Column(Integer)
