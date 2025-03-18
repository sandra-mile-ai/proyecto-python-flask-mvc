from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import session, Base

class Tipos(Base):
    __tablename__ ="tipos"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(300), unique=True, nullable=False)

    def __init__(self, tipo):
        self.tipo = tipo