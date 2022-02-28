from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

@app.get("/contacto")
def contacto():
    return render_template('contactos/index.html')

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