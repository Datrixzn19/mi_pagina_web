#nicio en flask



from flask import Flask
#con el debug on: no hace falta ir poniendo control s para ver cambios pero si recargar la paagina en el browser 
app = Flask(__name__)#este name indica que este archivo es el principal 
#flask --app nombreArhivo run   esto para levantar la aplicacion 
@app.route("/")#esto es un decorador con una ruta, cada ruta debe estar asociada a una funcion 
def hello():
    return "<p>Hello, Wsdfdsrd!</p>"
#activar el modo debug para mostrar errores, al levantar el server poner: flask --app nombreArhivo -- degub run
