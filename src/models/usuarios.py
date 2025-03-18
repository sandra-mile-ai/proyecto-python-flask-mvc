from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base 

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(15), nullable=False)
    direccion = Column(String(250), nullable=True)
    rol_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    facturas = relationship('Factura', back_populates='vendedor', cascade='all, delete-orphan')

    def __init__(self, nombre, email, telefono, direccion, rol_id):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.rol_id = rol_id

    def __repr__(self):
        return f'<Usuario {self.nombre} - Rol {self.rol_id}>'
