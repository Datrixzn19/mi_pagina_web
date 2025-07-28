#responder en varias rutas 



from flask import Flask

app = Flask(__name__)#

@app.route("/")
def index():
    return "<h1>Ruta base!</h1>"

#Segun vaya completando la ruta entrara a un u otro if 
@app.route("/hello")#
@app.route("/hello/<string:name>")#
@app.route("/hello/<string:name>/<int:edad>")#
def hello(name = None, edad = None):#dando valores por defecto 
    if name == None and edad == None:
        return "No ha enviado valores"
    elif edad == None:
        return f"Hola {name}, no has dado tu edad"
    else:
        return f"Hola {name}, tienes {edad} años"