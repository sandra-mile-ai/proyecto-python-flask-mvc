from src.app import app
from src.models import session
from flask import render_template, request, redirect, url_for, jsonify
from flask_controller import FlaskController
from src.models.usuarios import Usuarios 
from src.models.roles import Roles

class UsuariosController(FlaskController):
    @app.route('/crear_usuario', methods=['POST', 'GET'])
    def crear_usuario():
        if request.method == 'POST':
            try:
                nombre = request.form.get('nombre')
                email = request.form.get('email') 
                telefono = request.form.get('telefono')
                direccion = request.form.get('direccion')
                rol_id = request.form.get('roles')

                if not rol_id or rol_id == "Seleccione...":
                    return jsonify({"error": "Debes seleccionar un rol válido"}), 400 

                rol_id = int(rol_id) 
                
                usuario = Usuarios(nombre, email, telefono, direccion, rol_id)
                Usuarios.agregar_usuario(usuario)

                return redirect(url_for('ver_usuarios'))

            except Exception as e:
                return jsonify({"error": str(e)}), 500 

        roles = session.query(Roles).all()
        return render_template('formulario_crear_usuario.html', titulo_pagina='Crear Usuario', roles=roles)

    @app.route('/ver_usuarios')
    def ver_usuarios():
        usuarios = Usuarios.obtener_usuarios()
        return render_template('tabla_usuarios.html', titulo_pagina='ver_usuarios', usuarios=usuarios) 