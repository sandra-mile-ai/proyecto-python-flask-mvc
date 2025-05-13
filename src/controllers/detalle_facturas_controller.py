from flask import request, redirect, render_template, url_for
from src.app import app
from src.models import session
from flask_controller import FlaskController
from src.models.facturas import Facturas
from src.models.detalle_facturas import Detalle_Facturas
from src.models.productos import Productos
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios

class DetalleFacturasController(FlaskController):
    @app.route('/crear_detalle_facturas', methods=['GET', 'POST'])
    def crear_detalle_factura():
        if request.method == 'POST':
            try:
                cliente_id = int(request.form['cliente_id'])
                usuario_id = int(request.form['usuario_id'])
                producto_ids = request.form.getlist('producto_id')
                cantidades = request.form.getlist('cantidad')

                total_factura = 0.0
                detalles = []

                for prod_id, cantidad_str in zip(producto_ids, cantidades):
                    producto = session.query(Productos).get(int(prod_id))
                    cantidad = int(cantidad_str)
                    subtotal = producto.precio * cantidad
                    total_factura += subtotal

                    detalle = Detalle_Facturas(
                        factura_id=None,  # Se asigna después de guardar la factura
                        producto_id=producto.id_producto,
                        cantidad=cantidad,
                        precio_unitario=producto.precio
                    )
                    detalles.append(detalle)

                # Crear la factura
                factura = Facturas(
                    cliente_id=cliente_id,
                    usuario_id=usuario_id,
                    total=total_factura
                )
                session.add(factura)
                session.commit()

                # Asociar los detalles con la factura ya creada
                for detalle in detalles:
                    detalle.factura_id = factura.id
                    session.add(detalle)

                session.commit()
                return redirect(url_for('ver_facturas'))

            except Exception as e:
                session.rollback()
                return f"Error al crear la factura: {str(e)}", 500

        # GET method
        clientes = session.query(Clientes).all()
        usuarios = session.query(Usuarios).all()
        productos = session.query(Productos).all()

        return render_template(
            'formulario_factura.html',
            clientes=clientes,
            usuarios=usuarios,
            productos=productos
        )
