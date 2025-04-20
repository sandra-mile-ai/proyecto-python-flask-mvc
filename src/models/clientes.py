from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base, session
from src.models.tipos import Tipos

class Clientes(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(15), nullable=False)
    direccion = Column(String(250), nullable=True)
    
    tipo_id = Column(Integer, ForeignKey('tipos.id'), nullable=False)
    tipo = relationship("Tipos", backref="clientes")

    def __init__(self, nombre, email, telefono, direccion, tipo_id):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.tipo_id = tipo_id 

    def __repr__(self):
        tipo_nombre = self.tipo.nombre if self.tipo else "No asignado"
        return f'<Cliente {self.nombre} - Tipo {tipo_nombre}>'

    def tipo_str(self):
        return self.tipo.nombre if self.tipo else "No asignado"

    @staticmethod
    def agregar_clientes(cliente):
        session.add(cliente)
        session.commit()

    @staticmethod
    def obtener_clientes():
        return session.query(Clientes).all()

   