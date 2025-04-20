from src.app import app
from src.models import session
from flask import render_template, request, redirect, url_for, jsonify
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.categorias import Categorias

class ProductoController(FlaskController):
    @app.route('/crear_producto', methods=['POST', 'GET'])
    def crear_producto():
        if request.method == 'POST':
            try:
                descripcion = request.form.get('descripcion')
                valor_unitario = request.form.get('valor_unitario')
                unidad_medida = request.form.get('unidad_medida')
                cantidad_stock = request.form.get('cantidad_stock')
                categoria = request.form.get('categoria') 

                if not categoria or categoria == "Seleccione...":
                    return jsonify({"error": "Debes seleccionar una categoría válida"}), 400

                categoria = int(categoria)

                producto = Productos(descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria)
                Productos.agregar_producto(producto)

                return redirect(url_for('ver_productos'))

            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        categorias = session.query(Categorias).all()  
        return render_template('formulario_crear_producto.html', titulo_pagina='Crear Producto', categorias=categorias)
    
    @app.route('/ver_productos')
    def ver_productos():
        productos = Productos.obtener_productos()
        return render_template('tabla_productos.html', titulo_pagina = 'ver_productos', productos=productos)
