from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base

class detalle_facturas(Base):
    __tablename__ = 'detalle_facturas'

    id = Column(Integer, primary_key=True)
    factura_id = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id_producto'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    factura = relationship('factura', back_populates='detalles')

    def __init__(self, factura_id, producto_id, cantidad, precio_unitario):
        self.factura_id = factura_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = cantidad * precio_unitario 

    def __repr__(self):
        return f'<detalle_factura {self.id} - Factura {self.factura_id} - Producto {self.producto_id} - Cantidad {self.cantidad} - Subtotal {self.subtotal}>'
