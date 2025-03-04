from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_producto')
def crear_producto():
    return render_template('formulario_crear_producto.html')

@app.route('/ver_productos')
def ver_productos():
    return render_template('tabla_productos.html')

@app.route('/crear_cliente')
def crear_cliente():
    return render_template('formulario_crear_cliente.html')

@app.route('/ver_clientes')
def ver_clientes():
    return render_template('tabla_clientes.html')

@app.route('/crear_vendedor')
def crear_vendedor():
    return render_template('formulario_crear_vendedor.html')

@app.route('/ver_vendedores')  
def ver_vendedores(): 
    return render_template('tabla_vendedores.html')

@app.route('/crear_factura')
def crear_factura():
    return render_template('formulario_crear_factura.html')

@app.route('/ver_facturas')
def ver_facturas():
    return render_template('tabla_facturas.html')

if __name__ == '__main__':
    app.run(debug=True)
