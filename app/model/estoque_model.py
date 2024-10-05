from sqlalchemy import Column, Integer, ForeignKey
from app.db.conexao import Base

class Estoque(Base):
    __tablename__ = "estoque"

    id_cliente = Column(Integer(), ForeignKey("cliente.id"), primary_key=True, nullable=False)
    id_produto = Column(Integer(), ForeignKey("produto.id"), primary_key=True, nullable=False)
    quantity = Column(Integer(), nullable=False)
