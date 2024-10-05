from sqlalchemy import Column, Integer, String
from app.db.conexao import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer(),primary_key=True, nullable=False)
    nome = Column(String(), nullable=False)
    endereco = Column(String(), nullable=False)
    contato = Column(String(), nullable=False)
