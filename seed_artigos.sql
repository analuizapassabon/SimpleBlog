-- Script para adicionar dados de teste para o sistema de artigos

-- Inserir usuário autor@blog.com (senha: #Autor123)
-- Hash gerado para a senha #Autor123
INSERT OR IGNORE INTO usuario (nome, email, senha, perfil) 
VALUES ('Autor Blog', 'autor@blog.com', '$2b$12$YourHashHere', 'Autor');

-- Inserir categorias padrão
INSERT OR IGNORE INTO categoria (nome, descricao) VALUES 
('Tecnologia', 'Artigos sobre tecnologia, programação e inovação'),
('Tutoriais', 'Guias passo a passo e tutoriais práticos'),
('Notícias', 'Últimas notícias e atualizações'),
('Opinião', 'Artigos de opinião e análises'),
('Geral', 'Artigos diversos e variados');
