from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base
from datetime import datetime

class Facturas(Base):
    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, nullable=False)
    
    vendedor = relationship('Usuarios', back_populates='facturas')
    detalles = relationship('Detalle_Facturas', back_populates='factura')

    def __init__(self, cliente_id, usuario_id, total):
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id  
        self.total = total

    def __repr__(self):
        return f'<Factura {self.id} - Cliente {self.cliente_id} - Usuario {self.usuario_id} - fecha {self.fecha} - Total {self.total}>'
