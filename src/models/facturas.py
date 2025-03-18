from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base
from datetime import datetime

class Facturas(Base):
    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    vendedor_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, nullable=False)

    vendedor = relationship('Usuario', back_populates='facturas')

    def __init__(self, cliente_id, vendedor_id, total):
        self.cliente_id = cliente_id
        self.vendedor_id = vendedor_id
        self.total = total

    def __repr__(self):
        return f'<Factura {self.id} - Cliente {self.cliente_id} - Vendedor {self.vendedor_id} - Total {self.total}>'
