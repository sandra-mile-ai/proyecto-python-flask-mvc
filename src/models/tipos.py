from sqlalchemy import Column, Integer, String
from src.models import Base, session

class Tipos(Base):
    __tablename__ = "tipos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(300), unique=True, nullable=False)  

def __init__(self, nombre):
        self.tipos = nombre 

def obtener_tipos():
        tipos = session.query(Tipos).all()
        return tipos 