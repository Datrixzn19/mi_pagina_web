#renderizacion de plantillas

#Uso de filtros
#hay varios filtros aqui algunos:


from flask import Flask, render_template

app = Flask(__name__)#

@app.route("/")
def index():

    name = "David"
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 

    return render_template("index.html", name = name, numeros = numeros)







