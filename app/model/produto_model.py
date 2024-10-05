from sqlalchemy import Column, Integer, String
from app.db.conexao import Base

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer(), primary_key=True, nullable=False)
    nome = Column(String(), nullable=False)
    codigo = Column(String(), nullable=False)
    categoria = Column(String(), nullable=False)
