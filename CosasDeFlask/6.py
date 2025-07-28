#Manejo de varias rutas  

from flask import Flask

app = Flask(__name__)#

@app.route("/")
def index():
    return "<h1>Ruta base!</h1>"

@app.route("/hello")#
@app.route("/hello/<string:name>")#
@app.route("/hello/<string:name>/<int:edad>")#entrar a esta ruta o alguna anterior dependiendo de cuantos datos se ponga ruta/dato1/dato2/etc

def hello(name = None, edad = None):
    if name == None and edad == None:
        return "No ha enviado valores"
    elif edad == None:
        return f"Hola {name}, no has dado tu edad"
    else:
        return f"Hola {name}, tienes {edad} años"

