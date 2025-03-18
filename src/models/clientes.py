from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base

class Clientes(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(15), nullable=False)
    direccion = Column(String(250), nullable=True)
    tipo = Column(Integer, ForeignKey('tipos.id'), nullable=False)

    facturas = relationship('Factura', back_populates='vendedor', cascade='all, delete-orphan')

    def __init__(self, nombre, email, telefono, direccion, tipo):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.tipo = tipo

    def __repr__(self):
        return f'<cliente {self.nombre} - tipo {self.tipo}>'
