# Este es un comentario de una sola linea
'''
Este es un comenatrio de multiple lineas con comillas sencillas
'''
"""
Este es un comenatrio de multiple lineas con comillas dobles
"""

# Variables

nombre = 'Andres' # string
edad = 21 # int
numeroDecimal = 10.5 # float
mayorEdad = True # bool

# Debug

print(nombre) # Andres

# Array Arreglos Listas []

diasSemana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
arrayMultiple = [1, 'hola', [5,6]]

print(diasSemana)
print(arrayMultiple[2][1])

# Objetos JSON Diccionarios {}

persona = {
    'nombre': 'Andres',
    'apellido': 'Morales',
    'edad': 21,
    'lenguajes': ['Python', 'Javascript']
}

print(persona['nombre'],persona['apellido']) # Andres Morales
print(persona['lenguajes'][0]) # Python

# Listas de Diccionarios

personas = [
    persona,
    {
        'nombre': 'Lina',
        'apellido': 'Rodriguez',
        'edad': 19,
        'lenguajes': ['Go', 'Rust']
    },
    {
        'nombre': 'Goku',
        'apellido': 'Ssj',
        'edad': 25,
        'lenguajes': ['Java', '.Net']
    }
]

print(personas[1]['nombre'],personas[1]['lenguajes'][1])

# Condiciones

if mayorEdad == True:
    print(persona['nombre'],'Es mayor de edad')
else:
    print('No es mayor de edad')

print('fuera del else')