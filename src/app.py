from flask import Flask, render_template, request, redirect,url_for, jsonify
from src. models import Base, engine, session
from src.models.productos import Productos
from src.models.categorias import Categorias

app = Flask(__name__)

app = Flask(__name__)  
app.secret_key = "mi llaveria"  
app.debug = True

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = 'Inicio')

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
    try:
        productos = Productos.obtener_productos()

        return render_template('tabla_productos.html', titulo_pagina='Ver Productos', productos=productos)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  
