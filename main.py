from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'productos',
    port = '3306'
)
db.autocommit = True # Desactivar el cache

app = Flask(__name__)

@app.get("/")
def index():
    # Apertura del cursor, dictionary Treu formato leible
    cursor = db.cursor(dictionary = True)

    cursor.execute('SELECT * FROM productos')
    # Obtener todo lo de la consulta
    productos = cursor.fetchall()
    # print(productos[1]['nombre'])
    # Obtiene solo el primer valor de la consulta
    # productosOne = cursor.fetchone()

    # Cierre del cursor
    cursor.close()

    return render_template('index.html', productos = productos)

@app.get("/contacto")
def contacto():
    return render_template('contactos/index.html')

@app.get("/crear")
def crearProducto():
    return render_template("crear.html")

@app.post("/crear")
def crearProductoPost():
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')

    cursor = db.cursor()

    # ( nombre,precio) => tupla, lista no cambiante
    cursor.execute("INSERT INTO productos(nombre,precio) VALUES(%s,%s)",(
        nombre,
        precio,
    ))

    cursor.close()
    
    return redirect(url_for('index'))

@app.get("/contacto/<int:contactoId>/editar")
def editarContacto(contactoId):
    year = datetime.now().year
    # edad = year - int(contactoId)
    edad = year - contactoId
    return render_template(
        'contactos/editar.html',
        contactoId = contactoId,
        edad = edad
    )

app.run(debug=True)