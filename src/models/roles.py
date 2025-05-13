from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models import session, Base

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    rol = Column(String(300), unique=True, nullable=False)

    usuarios_relacion = relationship("Usuarios", back_populates="roles_relacion")
  

    def __init__(self, rol):
        self.rol = rol

    @staticmethod
    def obtener_roles():
        return session.query(Roles).all()
