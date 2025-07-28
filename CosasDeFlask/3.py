#RECIBIENDO VALORES POR URL


#OBTENER VALORES MEDIANTE LAS RUTAS 

from flask import Flask

app = Flask(__name__)#este name indica que este archivo es el principal 

@app.route("/")
def index():
    return "<h1>Ruta base!</h1>"

#Aqui name es el nombre de la variable que queremos recibir 
@app.route("/hello/<name>")#DE ESTA MANERA RECIBIMOS UN NOMBRE  http://127.0.0.1:5000/hello/valorEnviado
#para recibirlo lo ponemos como argumento a la funcion
def hello(name):
    return f"Hello, world!{name}"
