# Projeto Docker - Posts Simples

## Descrição

Aplicação web simples para gerenciar posts:

- Criar posts (título e conteúdo)
- Listar posts do mais recente para o mais antigo
- Deletar posts
- Frontend minimalista em HTML/CSS/JS
- Backend API RESTful em Flask
- Banco de dados PostgreSQL com persistência

Objetivo: aprendizado prático de Docker, redes de containers, volumes e variáveis de ambiente.

## Tecnologias

- Frontend: HTML, CSS, JavaScript
- Backend: Python 3.11 + Flask + SQLAlchemy + Flask-CORS
- Banco de dados: PostgreSQL 15
- Orquestração: Docker Compose
- Servidor frontend: Nginx

## Rodando o projeto

1. Criar arquivo `.env`:

POSTGRES_USER=meu_usuario
POSTGRES_PASSWORD=minha_senha_segura
POSTGRES_DB=meu_banco
DATABASE_URL=postgresql+psycopg2://meu_usuario:minha_senha_segura@db:5432/meu_banco

2. Build e subir containers:

docker compose up --build -d

3. Verificar status e logs:

docker compose ps
docker compose logs -f

4. Abrir frontend no navegador:

http://localhost:8080

## Endpoints da API

- GET /posts
  curl http://localhost:5000/posts

- POST /posts
  curl -X POST http://localhost:5000/posts \
   -H "Content-Type: application/json" \
   -d '{"title": "Novo post", "content": "Conteúdo"}'

- DELETE /posts/<id>
  curl -X DELETE http://localhost:5000/posts/1

- GET /health
  curl http://localhost:5000/health

## Backup e restore do banco

- Backup:
  docker exec -t postgres_db pg_dumpall -c -U $POSTGRES_USER > backup.sql

- Restore:
  cat backup.sql | docker exec -i postgres_db psql -U $POSTGRES_USER

## Observações sobre segurança

- Não versionar o arquivo `.env`
- Variáveis de ambiente armazenam credenciais, evitando hardcode no código
- `.gitignore` deve conter: `.env`, `venv/`, `__pycache__/`
