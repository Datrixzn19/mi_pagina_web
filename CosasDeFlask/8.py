#iNTRO A RENDERIZACION DE PLANTILLAS 

from flask import Flask, render_template#IMPORTAR ESTA FUNCION del modulo flask

app = Flask(__name__)#

@app.route("/")
def index():
    #podemos enviar variables y debemos ponerlas dentro del rendertemplate de la forma que se muestra, no se puede enviar de manera directa sino debemos crearla y luego pasarla a render
    name = "David"
    #en el index html las variables de ponen dentro de: {{}}
    #ej.   <h1>Bienvenido, {{ name }}</h1>

    #usamos render_template y dentro la ruta, en este caso solo ponemos indexhtml porque esta dentro de la carpeta templates y flask ya busca siempre alli
    return render_template("index.html", name = name)