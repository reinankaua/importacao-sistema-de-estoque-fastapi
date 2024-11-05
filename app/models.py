from sql import Column, Integer, String
from .database import Base

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    codigo = Column(String(50), unique=True, index=True)
    categoria = Column(String(100))