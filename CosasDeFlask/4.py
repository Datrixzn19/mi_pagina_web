#recibir mas de un valor por las rutas 

#Recibiendo valores por url
#por defecto recibimos strings 
from flask import Flask

app = Flask(__name__)#

@app.route("/")
def index():
    return "<h1>Ruta base!</h1>"


#por defecto recibimos strings, pero podmeos recibir:
# int
# float
# path que es que recibe caracteres especiales y los pone en string
# uuid es un string largo como una contrase;a, Se usa para garantizar que un ID sea único en cualquier sistema, sin necesidad de una base de datos central. 
@app.route("/hello/<string:name>/<int:edad>")#asi definimos que vamos a recibir, asi se recibe mas de uno
#en la ruta poner /hello/getNombre/getEdad
def hello(name, edad):
    return f"Hola {name}, tienes {edad} años"

