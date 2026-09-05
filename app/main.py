from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from app.database import Base, engine, get_db
from app.models import FilmeDB
from sqlalchemy.orm import Session 

app = FastAPI()
Base.metadata.create_all(bind=engine)

class Filme(BaseModel):
    titulo: str
    titulo_original: str
    data_lancamento: str
    diretores: list[str]
    sinopse: str

class FilmeResposta(BaseModel):
    id: int
    titulo: str
    titulo_original: str
    data_lancamento: str
    sinopse: str

    class Config:
        from_attributes = True

filme_info = Filme(
    titulo = "Vingadores: Doutor Destino",
    titulo_original = "Avengers: Doomsday",
    data_lancamento = "18-12-2026",
    diretores = ["Anthony Russo", "Joe Russo"],
    sinopse = "Em Vingadores: Doutor Destino, heróis queridos de três universos distintos entrarão em rota de colisão e enfrentarão uma ameaça existencial sem precedentes"
)

@app.get("/")
def raiz():
    return {"mensagem": "API do Vingadores: Doomsday está rodando!"}

@app.get("/filme", response_model = list[FilmeResposta])
def listar_filmes(db: Session = Depends(get_db)):
    return db.query(FilmeDB).all()

@app.post("/filme", response_model=FilmeResposta)
def criar_filme(filme: Filme, db: Session = Depends(get_db)):
    novo_filme = FilmeDB(
        titulo=filme.titulo,
        titulo_original=filme.titulo_original,
        data_lancamento=filme.data_lancamento,
        sinopse=filme.sinopse,
    )
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

@app.delete("/filme/{filme_id}")
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(FilmeDB).filter(FilmeDB.id == filme_id).first()
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    db.delete(filme)
    db.commit()
    return {"mensagem": f"Filme {filme_id} deletado com sucesso"}

@app.put("/filme/{filme_id}", response_model=FilmeResposta)
def atualizar_filme(filme_id: int, filme_atualizado: Filme, db: Session = Depends(get_db)):
    filme = db.query(FilmeDB).filter(FilmeDB.id == filme_id).first()
    if filme is None: 
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    filme.titulo = filme_atualizado.titulo
    filme.titulo_original = filme_atualizado.titulo_original
    filme.data_lancamento = filme_atualizado.data_lancamento
    filme.sinopse = filme_atualizado.sinopse

    db.commit()
    db.refresh(filme)
    return filme