from src.app import app
from src.models import session
from flask import render_template, request, redirect, url_for, jsonify
from flask_controller import FlaskController
from src.models.clientes import Clientes
from src.models.tipos import Tipos

class ClienteController(FlaskController):
    @app.route('/crear_cliente', methods=['POST', 'GET'])
    def crear_cliente():
        if request.method == 'POST':
            try:
                nombre = request.form.get('nombre')
                email = request.form.get('email')
                telefono = request.form.get('telefono')
                direccion = request.form.get('direccion')
                tipo_id = request.form.get('tipos')

                if not tipo_id or tipo_id == "Seleccione...":
                    return jsonify({"error": "Debes seleccionar un tipo válido"}), 400

                tipo_id = int(tipo_id) 
                
                cliente = Clientes(nombre, email, telefono, direccion, tipo_id)
                Clientes.agregar_clientes(cliente)

                return redirect(url_for('ver_clientes'))

            except Exception as e:
                return jsonify({"error": str(e)}), 500 

        tipos = session.query(Tipos).all()
        return render_template('formulario_crear_cliente.html', titulo_pagina='Crear Cliente', tipos=tipos)

    @app.route('/ver_clientes')
    def ver_clientes():
        clientes = Clientes.obtener_clientes()
        return render_template('tabla_clientes.html', titulo_pagina='ver_clientes', clientes=clientes) 
