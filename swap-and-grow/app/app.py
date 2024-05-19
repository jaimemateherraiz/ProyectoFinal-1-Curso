from flask import Flask, render_template, request, redirect, url_for
from conexion_db import DatabaseConnection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplace', methods=['GET', 'POST'])
def marketplace():
    if request.method == 'POST':
        # Procesar datos del formulario y agregarlos a la base de datos
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        # Aquí iría el código para agregar los datos a la base de datos

    # Obtener productos de la base de datos
    try:
        with DatabaseConnection() as db:
            productos = db.execute_query("SELECT identificador, nombre, descripcion, precio FROM productos")
            if productos is None:
                productos = []
            print("Productos obtenidos de la base de datos:", productos)
    except Exception as e:
        print(f"Error al acceder a la base de datos: {e}")
        productos = []

    return render_template('marketplace.html', productos=productos)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
