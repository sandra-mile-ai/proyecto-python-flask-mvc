from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models import session, Base
from src.models.roles import Roles

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(250), nullable=True)
    rol_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    roles_relacion = relationship("Roles", back_populates="usuarios_relacion")

    facturas = relationship('Facturas', back_populates='vendedor')

    def __init__(self, nombre, email, telefono, direccion, rol_id):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.rol_id = rol_id

    def __repr__(self):
        rol_nombre = self.roles_relacion.rol if self.roles_relacion else "Sin rol"
        return f"<Usuario {self.nombre} - Rol {rol_nombre}>"

    def rol_str(self):
        return self.roles_relacion.rol if self.roles_relacion else "Sin rol"

    @staticmethod
    def obtener_usuarios():
        return session.query(Usuarios).all()

    @staticmethod
    def agregar_usuario(usuario):
        session.add(usuario)
        session.commit()
