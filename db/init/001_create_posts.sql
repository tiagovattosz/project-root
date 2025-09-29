-- Criação da tabela posts
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Seed inicial com 2 registros
INSERT INTO posts (title, content)
VALUES
    ('Primeiro Post', 'Este é o conteúdo do primeiro post de teste.'),
    ('Segundo Post', 'Este é o conteúdo do segundo post de exemplo.');
