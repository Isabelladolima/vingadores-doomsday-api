# Ⓐ Vingadores: Doomsday API

API REST desenvolvida em **Python + FastAPI**, com integração à API pública do **TMDb (The Movie Database)**, criada como projeto de portfólio e estudo de backend.

O projeto gira em torno do filme **Vingadores: Doomsday** (estreia em 18/12/2026), oferecendo dados sobre o filme e seu elenco, com persistência local em banco de dados.

## Funcionalidades

- **CRUD completo de Filmes** — criar, listar, atualizar e deletar informações sobre o filme
- **Integração com a API do TMDb** — busca de filmes por nome e elenco em tempo real
- **CRUD de Elenco** — criação manual de membros do elenco, listagem, e importação automática em massa a partir do TMDb
- **Documentação interativa automática** via Swagger UI (`/docs`)
- **Validação de dados** com Pydantic
- **Persistência em banco de dados** SQLite via SQLAlchemy ORM

## Tecnologias utilizadas

- [Python 3.12](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — framework web
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [SQLite](https://www.sqlite.org/) — banco de dados
- [Pydantic](https://docs.pydantic.dev/) — validação de dados
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente
- [Requests](https://docs.python-requests.org/) — chamadas HTTP
- [TMDb API](https://www.themoviedb.org/documentation/api) — dados reais de filmes e elenco

## 📂 Estrutura do projeto

vingadores-doomsday-api/
├── app/
│ ├── main.py # Rotas da API
│ ├── database.py # Configuração de conexão com o banco
│ ├── models.py # Modelos das tabelas (SQLAlchemy)
│ └── tmdb_service.py # Integração com a API do TMDb
├── requirements.txt # Dependências do projeto
├── .env # Variáveis de ambiente (não versionado)
├── .gitignore
└── README.md


## Como rodar o projeto localmente

### Pré-requisitos
- Python 3.10 ou superior
- Uma chave de API gratuita do [TMDb](https://www.themoviedb.org/settings/api)

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/Isabelladolima/vingadores-doomsday-api.git
cd vingadores-doomsday-api
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com sua chave do TMDb:
```bash
TMDB_API_KEY=sua_chave_aqui
```

6. Rode o servidor:
```bash
uvicorn app.main:app --reload
```

6. Acesse a documentação interativa:
```bash
http://127.0.0.1:8000/docs
```

## Principais endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/filme` | Lista todos os filmes salvos |
| POST | `/filme` | Cria um novo filme |
| PUT | `/filme/{filme_id}` | Atualiza um filme existente |
| DELETE | `/filme/{filme_id}` | Remove um filme |
| GET | `/tmdb/buscar` | Busca um filme pelo nome direto no TMDb |
| GET | `/tmdb/elenco` | Busca o elenco de um filme direto no TMDb |
| POST | `/tmdb/elenco/{tmdb_id}/salvar` | Importa e salva o elenco de um filme do TMDb no banco local |
| GET | `/elenco` | Lista o elenco salvo no banco |
| POST | `/elenco` | Adiciona um membro do elenco manualmente |

## Próximos passos

- [ ] Aparições históricas do Doutor Destino nos quadrinhos (API da Marvel)
- [ ] Sistema de teorias e discussão da comunidade, com autenticação de usuários
- [ ] Deploy em serviço gratuito (Railway/Render)

## Autora

Desenvolvido por **Isabella de Lima** como projeto de estudo e portfólio em desenvolvimento backend.

---

> Dados de filmes e elenco fornecidos pela API do [TMDb](https://www.themoviedb.org/). Este produto usa a API do TMDb, mas não é endossado ou certificado pelo TMDb.
