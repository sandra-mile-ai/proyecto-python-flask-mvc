from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import session, Base

class roles(Base):
    __tablename__ ="roles"
    id = Column(Integer, primary_key=True)
    rol = Column(String(300), unique=True, nullable=False)

    def __init__(self, rol):
        self.rol = rol 