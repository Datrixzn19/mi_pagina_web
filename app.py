#renderizacion de plantillas

#Herencia de plantillas 

#nos sirve para que el codigo que tengamos que repetir(como un menu de navegacion) lo guardemos en un archivo y lo podamos usar luego
#a ese archivo normalmente se lo llama base.html y se lo pone en la carpeta templates 

from flask import Flask, render_template

app = Flask(__name__)#

@app.route("/")
def index():

    name = "David"
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 

    return render_template("index.html", name = name, numeros = numeros)


"""en este caso no necesitamos hacer en python ya que las plantillas se crean y heredan en html"""







