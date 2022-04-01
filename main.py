from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

from models import productos_models

app = Flask(__name__)

app.secret_key = '#andSecretKey'

@app.get("/")
def index():
    productos = productos_models.obtenerProductos()
    return render_template('index.html', productos=productos)

@app.get("/contacto")
def contacto():
    return render_template('contactos/index.html')

@app.get("/crear")
def crearProducto():
    return render_template("crear.html")

@app.post("/crear")
def crearProductoPost():
    nombre = request.form.get('nombre')
    try:
        precio = int(request.form.get('precio'))
    except:
        precio = 0
    
    isValid = True

    if nombre == "":
        isValid = False
        flash("El nombre es obligatorio")

    if precio <= 0:
        isValid = False
        flash("El precio es obligatorio y debe ser mayor o igual a cero")

    if isValid == False:
        return render_template("crear.html", nombre = nombre, precio = precio)

    productos_models.crearProducto(nombre=nombre, precio=precio)
    
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