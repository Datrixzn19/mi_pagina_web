#renderizacion de plantillas

#creacion de funciones personalizadas

from flask import Flask, render_template
 

app = Flask(__name__)


def repeticion(string, numeroRepeticiones):
    return string * numeroRepeticiones
#hay tres formas de enviarla
        #primera forma
"""

def repeticion(string, numeroRepeticiones):
    return string * numeroRepeticiones

#si usamos esta manera en el render_template deberemos hacer el repeticion = repeticion
"""
        #segunda forma
#tambien podemos enviarla por medio de un decorador 
"""
@app.add_template_global
def repeticion(string, numeroRepeticiones):
    return string * numeroRepeticiones

"""
        #tercera forma 
app.add_template_global(repeticion)

@app.route("/")
def index():

    name = "David"
   
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 

    return render_template("index.html",#podemos organizar si son muchas variables
                             name = name,
                             numeros = numeros,                             
                             )










