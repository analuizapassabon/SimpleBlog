"""
Script para adicionar dados de teste para o sistema de artigos
"""
from repo import usuario_repo, categoria_repo
from model.usuario_model import Usuario
from model.categoria_model import Categoria
from util.security import criar_hash_senha
from util.perfis import Perfil

def adicionar_usuario_autor():
    """Adiciona o usuário autor@blog.com"""
    # Verificar se já existe
    usuario_existente = usuario_repo.obter_por_email("autor@blog.com")
    if usuario_existente:
        print(f"✓ Usuário autor@blog.com já existe (ID: {usuario_existente.id})")
        return usuario_existente.id
    
    # Criar novo usuário
    usuario = Usuario(
        id=0,
        nome="Autor Blog",
        email="autor@blog.com",
        senha=criar_hash_senha("#Autor123"),
        perfil=Perfil.AUTOR.value
    )
    
    usuario_id = usuario_repo.inserir(usuario)
    if usuario_id:
        print(f"✓ Usuário autor@blog.com criado com sucesso (ID: {usuario_id})")
        print(f"  Email: autor@blog.com")
        print(f"  Senha: #Autor123")
        return usuario_id
    else:
        print("✗ Erro ao criar usuário autor@blog.com")
        return None

def adicionar_categorias():
    """Adiciona categorias padrão"""
    categorias_padrao = [
        ("Tecnologia", "Artigos sobre tecnologia, programação e inovação"),
        ("Tutoriais", "Guias passo a passo e tutoriais práticos"),
        ("Notícias", "Últimas notícias e atualizações"),
        ("Opinião", "Artigos de opinião e análises"),
        ("Geral", "Artigos diversos e variados"),
    ]
    
    categorias_criadas = 0
    
    for nome, descricao in categorias_padrao:
        # Verificar se já existe
        categorias_existentes = categoria_repo.obter_todos()
        ja_existe = any(c.nome == nome for c in categorias_existentes)
        
        if ja_existe:
            print(f"  Categoria '{nome}' já existe")
            continue
        
        # Criar nova categoria
        categoria = Categoria(
            id=0,
            nome=nome,
            descricao=descricao
        )
        
        categoria_id = categoria_repo.inserir(categoria)
        if categoria_id:
            print(f"✓ Categoria '{nome}' criada (ID: {categoria_id})")
            categorias_criadas += 1
        else:
            print(f"✗ Erro ao criar categoria '{nome}'")
    
    if categorias_criadas > 0:
        print(f"\n✓ {categorias_criadas} categoria(s) criada(s) com sucesso!")
    else:
        print("\n  Todas as categorias já existiam")

if __name__ == "__main__":
    print("=" * 60)
    print("ADICIONANDO DADOS DE TESTE PARA O SISTEMA DE ARTIGOS")
    print("=" * 60)
    print()
    
    print("1. Criando usuário autor...")
    adicionar_usuario_autor()
    print()
    
    print("2. Criando categorias padrão...")
    adicionar_categorias()
    print()
    
    print("=" * 60)
    print("CONCLUÍDO!")
    print("=" * 60)
    print()
    print("Você pode fazer login com:")
    print("  Email: autor@blog.com")
    print("  Senha: #Autor123")
