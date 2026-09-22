from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from app.database import Base, engine, get_db
from app.models import FilmeDB, ElencoDB, AparicaoQuadrinhoDB
from sqlalchemy.orm import Session 
from app.tmdb_service import buscar_filme_por_nome, buscar_elenco
from app.comicvine_service import buscar_personagem, buscar_aparicoes

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

class Elenco(BaseModel):
    pessoa_id: int
    nome: str
    personagem: str
    foto_path: str
    ordem: int

class ElencoResposta(BaseModel):
    id: int
    pessoa_id: int
    nome: str
    personagem: str
    foto_path: str
    ordem: int

    class Config:
        from_attributes = True

class AparicaoResposta(BaseModel):
    id: int
    issue_id: int
    titulo: str
    url: str
    
    class Config:
        from_attributes = True

@app.get("/")
def raiz():
    return {"mensagem": "API do Vingadores: Doomsday está rodando!"}

@app.get("/filme", response_model = list[FilmeResposta])
def listar_filmes(db: Session = Depends(get_db)):
    return db.query(FilmeDB).all()

@app.get("/aparicao", response_model = list[AparicaoResposta])
def listar_aparicao(db: Session = Depends(get_db)):
    return db.query(AparicaoQuadrinhoDB).all()

@app.get("/tmdb/buscar")
def buscar_no_tmdb(nome: str):
    resultado = buscar_filme_por_nome(nome)
    return resultado 

@app.get("/tmdb/elenco")
def mostrar_elenco(tmdb_id: int):
    resultado = buscar_elenco(tmdb_id)
    return resultado

@app.get("/elenco", response_model = list[ElencoResposta])
def listar_elenco(db: Session = Depends(get_db)):
    return db.query(ElencoDB).all()

@app.get("/comicvine/buscar")
def buscar_no_comicvine(nome: str):
    resultado = buscar_personagem(nome)
    return resultado

@app.get("/comicvine/buscar_aparicoes")
def buscar_aparicoes_comicvine(nome_id: int):
    resultado = buscar_aparicoes(nome_id)
    return resultado

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


@app.post("/elenco", response_model = ElencoResposta)
def criar_elenco(elenco: Elenco, db: Session = Depends(get_db)):
    novo_elenco = ElencoDB(
        pessoa_id = elenco.pessoa_id,
        nome = elenco.nome,
        personagem = elenco.personagem,
        foto_path = elenco.foto_path,
        ordem = elenco.ordem,
    )
    db.add(novo_elenco)
    db.commit()
    db.refresh(novo_elenco)
    return novo_elenco

@app.post("/tmdb/elenco/{tmdb_id}/salvar")
def salvar_elenco(tmdb_id: int, db: Session = Depends(get_db)):
    dados = buscar_elenco(tmdb_id)

    for pessoa in dados["cast"]:
        novo_membro = ElencoDB(
            pessoa_id = pessoa["id"],
            nome = pessoa["name"],
            personagem = pessoa["character"],
            foto_path = pessoa ["profile_path"],
            ordem = pessoa["order"]
        )
        db.add(novo_membro)

    db.commit()
    return {"mensagem": "Elenco salvo com sucesso!"}

@app.post("/comicvine/aparicoes/{personagem_id}/salvar")
def salvar_aparicao(personagem_id: int, db: Session = Depends(get_db)):
    dados = buscar_aparicoes(personagem_id)

    for item in dados["results"]["issue_credits"]:
        nova_aparicao = AparicaoQuadrinhoDB(
            issue_id = item["id"],
            titulo = "",
            url = item["site_detail_url"]
        )
        db.add(nova_aparicao)

    db.commit()
    return {"mensagem": "Aparição salva com sucesso!"}


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