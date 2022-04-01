from config.database import db

def obtenerProductos():
    cursor = db.cursor(dictionary = True)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    cursor.close()
    return productos

def crearProducto(nombre,precio):
    cursor = db.cursor()
    cursor.execute("INSERT INTO productos(nombre,precio) VALUES(%s,%s)",(
        nombre,
        precio,
    ))
    cursor.close()