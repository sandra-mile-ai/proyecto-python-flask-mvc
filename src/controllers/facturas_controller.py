from flask import request, redirect, render_template, url_for
from src.app import app
from src.models import session
from datetime import datetime
from flask_controller import FlaskController
from src.models.facturas import Facturas
from src.models.detalle_facturas import Detalle_Facturas
from src.models.productos import Productos 
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios

class FacturasController(FlaskController):    
    @app.route('/crear_factura', methods=['GET', 'POST'])
    def crear_factura():
        if request.method == 'POST':
            cliente_id = int(request.form['cliente_id'])
            usuario_id = int(request.form['usuario_id'])
            producto_ids = request.form.getlist('producto_id')
            cantidades = request.form.getlist('cantidad')

            total = 0
            detalles = []

            for prod_id, cant in zip(producto_ids, cantidades):
                producto = session.query(Productos).get(int(prod_id))
                cantidad = int(cant)
                subtotal = cantidad * producto.precio
                detalle = Detalle_Facturas(
                    factura_id=0,  # Se actualiza luego
                    producto_id=producto.id_producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )
                detalles.append(detalle)
                total += subtotal

            factura = Facturas(cliente_id=cliente_id, usuario_id=usuario_id, total=total)
            session.add(factura)
            session.commit()

            for detalle in detalles:
                detalle.factura_id = factura.id
                session.add(detalle)

            session.commit()
            return redirect(url_for('ver_facturas'))
        
        clientes = session.query(Clientes).all()
        productos = session.query(Productos).all()
        usuarios = session.query(Usuarios).all()

        return render_template(
            'formulario_crear_factura.html',
            clientes=clientes,
            productos=productos,
            usuarios=usuarios
        ) 
