<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:1A3A2E,100:2ECC71&height=200&section=header&text=Vingadores:%20Doomsday%20API&fontSize=38&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=Victor%20Von%20Doom%20%7C%20Monarquia%20de%20Latveria&descAlignY=55&descSize=16&descColor=7FD99A" width="100%"/>

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-2ECC71?style=for-the-badge&logoColor=white)
![Python](https://img.shields.io/badge/-Python-0D0D0D?style=for-the-badge&logo=python&logoColor=2ECC71)
![FastAPI](https://img.shields.io/badge/-FastAPI-0D0D0D?style=for-the-badge&logo=fastapi&logoColor=2ECC71)
![JWT](https://img.shields.io/badge/-JWT-0D0D0D?style=for-the-badge&logo=jsonwebtokens&logoColor=2ECC71)

</div>

> *"Todo mundo pensa que eu sou o vilão. Eles simplesmente não entendem a minha visão."* — Victor Von Doom

API REST desenvolvida em **Python + FastAPI**, com integração a múltiplas APIs externas (**TMDb** e **Comic Vine**) e autenticação de usuários via **JWT**. Criada como projeto de portfólio e estudo de backend, girando em torno do filme **Vingadores: Doomsday** (estreia em 18/12/2026).

<br/>

## Funcionalidades

<details open>
<summary><b>Filmes</b></summary>
<br/>

CRUD completo — criar, listar, atualizar e deletar informações sobre o filme.

</details>

<details open>
<summary><b>Elenco — integração com TMDb</b></summary>
<br/>

Busca de filmes e elenco em tempo real na API do TMDb, com importação automática em massa e CRUD completo dos registros salvos localmente.

</details>

<details open>
<summary><b>Aparições em quadrinhos — integração com Comic Vine</b></summary>
<br/>

Busca de personagens e suas aparições em edições de quadrinhos reais via API da Comic Vine, com importação automática e persistência local.

</details>

<details open>
<summary><b>Autenticação de usuários</b></summary>
<br/>

Cadastro com senha protegida por hash (**bcrypt**) e login com emissão de token **JWT**, para proteger rotas restritas a usuários autenticados.

</details>

- **Documentação interativa automática** via Swagger UI (`/docs`)
- **Validação de dados** com Pydantic
- **Persistência em banco de dados** SQLite via SQLAlchemy ORM

<br/>

## Tecnologias utilizadas

<div align="center">

![Python](https://img.shields.io/badge/Python-0D0D0D?style=for-the-badge&logo=python&logoColor=2ECC71)
![FastAPI](https://img.shields.io/badge/FastAPI-0D0D0D?style=for-the-badge&logo=fastapi&logoColor=2ECC71)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-0D0D0D?style=for-the-badge&logo=sqlalchemy&logoColor=2ECC71)
![SQLite](https://img.shields.io/badge/SQLite-0D0D0D?style=for-the-badge&logo=sqlite&logoColor=2ECC71)
![Pydantic](https://img.shields.io/badge/Pydantic-0D0D0D?style=for-the-badge&logo=pydantic&logoColor=2ECC71)
![JSONWebTokens](https://img.shields.io/badge/JWT-0D0D0D?style=for-the-badge&logo=jsonwebtokens&logoColor=2ECC71)

</div>

| Tecnologia | Papel no projeto |
|---|---|
| [Python 3.12](https://www.python.org/) | Linguagem principal |
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM |
| [SQLite](https://www.sqlite.org/) | Banco de dados |
| [Pydantic](https://docs.pydantic.dev/) | Validação de dados |
| [python-jose](https://pypi.org/project/python-jose/) | Geração e validação de tokens JWT |
| [passlib + bcrypt](https://pypi.org/project/passlib/) | Hash seguro de senhas |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Variáveis de ambiente |
| [Requests](https://docs.python-requests.org/) | Chamadas HTTP |
| [TMDb API](https://www.themoviedb.org/documentation/api) | Dados reais de filmes e elenco |
| [Comic Vine API](https://comicvine.gamespot.com/api/) | Dados reais de quadrinhos e personagens |

<br/>

## 📂 Estrutura do projeto

```
vingadores-doomsday-api/
├── app/
│   ├── main.py                 # Rotas da API
│   ├── database.py             # Configuração de conexão com o banco
│   ├── models.py                # Modelos das tabelas (SQLAlchemy)
│   ├── auth.py                    # Hash de senha, geração e validação de JWT
│   ├── tmdb_service.py        # Integração com a API do TMDb
│   └── comicvine_service.py   # Integração com a API do Comic Vine
├── requirements.txt        # Dependências do projeto
├── .env                     # Variáveis de ambiente (não versionado)
├── .gitignore
└── README.md
```

</details>

<br/>

## Principais endpoints

<details>
<summary><b>Filmes</b></summary>
<br/>

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/filme` | Lista todos os filmes salvos |
| POST | `/filme` | Cria um novo filme |
| PUT | `/filme/{filme_id}` | Atualiza um filme existente |
| DELETE | `/filme/{filme_id}` | Remove um filme |

</details>

<details>
<summary><b>Elenco & TMDb</b></summary>
<br/>

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tmdb/buscar` | Busca um filme pelo nome direto no TMDb |
| GET | `/tmdb/elenco` | Busca o elenco de um filme direto no TMDb |
| POST | `/tmdb/elenco/{tmdb_id}/salvar` | Importa e salva o elenco do TMDb no banco local |
| GET | `/elenco` | Lista o elenco salvo no banco |
| POST | `/elenco` | Adiciona um membro do elenco manualmente |

</details>

<details>
<summary><b>Quadrinhos & Comic Vine</b></summary>
<br/>

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/comicvine/buscar` | Busca um personagem pelo nome direto no Comic Vine |
| GET | `/comicvine/aparicoes` | Busca aparições de um personagem direto no Comic Vine |
| POST | `/comicvine/aparicoes/{personagem_id}/salvar` | Importa e salva as aparições no banco local |
| GET | `/aparicao` | Lista as aparições salvas no banco |

</details>

<details>
<summary><b>Autenticação</b></summary>
<br/>

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/usuarios/cadastro` | Cadastra um novo usuário (senha protegida por hash) |
| POST | `/usuarios/login` | Autentica e retorna um token JWT |

</details>

<br/>

## Próximos passos

- [ ] Sistema de teorias e discussão da comunidade, com rotas protegidas por autenticação
- [ ] Deploy em serviço gratuito (Railway/Render)

<br/>

## Autora

Desenvolvido por **Isabella Lima** como projeto de estudo e portfólio em desenvolvimento backend.

<div align="center">

<a href="https://www.linkedin.com/in/isabelladolima/">
  <img src="https://img.shields.io/badge/LinkedIn-1A3A2E?style=for-the-badge&logo=linkedin&logoColor=2ECC71"/>
</a>
<a href="https://github.com/Isabelladolima">
  <img src="https://img.shields.io/badge/GitHub-0D0D0D?style=for-the-badge&logo=github&logoColor=2ECC71"/>
</a>

</div>

---

> Dados de filmes e elenco fornecidos pela API do [TMDb](https://www.themoviedb.org/). Dados de quadrinhos fornecidos pela API do [Comic Vine](https://comicvine.gamespot.com/). Este produto usa essas APIs, mas não é endossado ou certificado por nenhuma delas.

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:1A3A2E,100:2ECC71&height=100&section=footer" width="100%"/>
</div>
