from sql import Session
from . import models, schemas

# Função para obter um produto específico pelo ID
def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

# Função para obter uma lista de produtos, com suporte a paginação
def get_produtos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Produto).offset(skip).limit(limit).all()

# Função para criar um novo produto
def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(nome=produto.nome, codigo=produto.codigo, categoria=produto.categoria)
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

# Função para atualizar um produto existente
def update_produto(db: Session, produto_id: int, produto: schemas.ProdutoCreate):
    db_produto = get_produto(db, produto_id)
    if db_produto is None:
        return None
    db_produto.nome = produto.nome
    db_produto.codigo = produto.codigo
    db_produto.categoria = produto.categoria
    db.commit()
    db.refresh(db_produto)
    return db_produto

# Função para deletar um produto
def delete_produto(db: Session, produto_id: int):
    db_produto = get_produto(db, produto_id)
    if db_produto is None:
        return None
    db.delete(db_produto)
    db.commit()
    return db_produto