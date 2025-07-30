#uso de filtros

#permite transformar valores antes de mostrarlos

#tiene esta sintaxis  {{ nombreVariable | nombreFiltro }}

from flask import Flask, render_template

app = Flask(__name__)#

@app.route("/")
def index():

    name = "David"
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 

    return render_template("index.html", name = name, numeros = numeros)


"""
{%extends "base.html"%}

   
    <h1>Bienvenido, {{ name | upper }}</h1>
    <h1>Hola, {{ name | first }}</h1>
    
    <ul>
        <!--asi imprimimos una lista desde python-->
        {%for numero in numeros | reverse %}
            <li> {{ numero }} </li> 
        {% endfor %}

    </ul>


   
    {% endblock%}
"""

