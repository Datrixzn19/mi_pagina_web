#renderizacion de plantillas

#creacion de filtros personalizadas

from flask import Flask, render_template
from datetime import datetime#para hacer el ejemplo de personalizar plantillas 

app = Flask(__name__)



#filtros personalizados
#forma numero uno:
"""
@app.add_template_filter#necesitamos esto para que jinja lo reconozca
def hoy(fecha):
    return fecha.strftime("%a-%B-%Y %M-%S")
#en html usamos el nombreVariable | NombreFiltro en este caso es "hoy"



"""
#forma numero 2

def hoy(fecha):
    return fecha.strftime("%a-%B-%Y %M-%S")
#ojo no poner el @ en app
app.add_template_filter(hoy, "hoy") #nombre de la funcion, nombre de como la vamos a llamar








@app.route("/")
def index():

    name = "David"
    fecha = datetime.now()
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 

    return render_template("index.html",#podemos organizar si son muchas variables
                             name = name,
                             numeros = numeros,
                             fecha = fecha)










