from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Base, Post
from os import getenv
import os

app = Flask(__name__)

frontend_url = getenv("FRONTEND_URL", "*")  # permite definir a URL depois
CORS(app, origins=[frontend_url])


# Configurações do banco via variáveis de ambiente
DB_URL = os.environ.get("DATABASE_URL")
if not DB_URL:
    raise RuntimeError("❌ A variável DATABASE_URL não está definida!")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

# Cria as tabelas se não existirem
Base.metadata.create_all(engine)

# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "API is running"}), 200

# Listar posts (mais recentes primeiro)
@app.route("/posts", methods=["GET"])
def get_posts():
    session = SessionLocal()
    posts = session.query(Post).order_by(Post.created_at.desc()).all()
    result = [{"id": p.id, "title": p.title, "content": p.content, "created_at": p.created_at.isoformat()} for p in posts]
    session.close()
    return jsonify(result), 200

# Criar post
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400

    session = SessionLocal()
    new_post = Post(title=title, content=content)
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    session.close()

    return jsonify({"id": new_post.id, "title": new_post.title, "content": new_post.content, "created_at": new_post.created_at.isoformat()}), 201

# Deletar post
@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    session = SessionLocal()
    post = session.get(Post, post_id)
    if not post:
        session.close()
        return jsonify({"error": "Post not found"}), 404

    session.delete(post)
    session.commit()
    session.close()
    return jsonify({"message": "Post deleted successfully", "id": post_id}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
