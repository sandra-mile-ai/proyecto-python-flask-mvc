from flask import Flask, render_template, request, redirect,url_for, jsonify
from src. models import Base, engine, session
from datetime import datetime
from  flask_controller import FlaskControllerRegister
from src.models.productos import Productos
from src.models.categorias import Categorias
from src.models.clientes import Clientes 
from src.models.tipos import Tipos
from src.models.usuarios import Usuarios
from src.models.roles import Roles 
from src.models.facturas import Facturas
from src.models.detalle_facturas import Detalle_Facturas 

app = Flask(__name__) 

app.secret_key = "mi llaveria"  
app.debug = True

Base.metadata.create_all(engine) 

register = FlaskControllerRegister(app)
register.register_package('src.controllers') 

if __name__ == '__main__':
    app.run(debug=True) 