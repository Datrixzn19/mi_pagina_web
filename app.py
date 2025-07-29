#renderizacion de plantillas

#uso de mas variables y datos 

#no solo podemos enviar variables sino otros tipos de datos
#vamos a hacer el ejemplo enviando listas 
from flask import Flask, render_template

app = Flask(__name__)#

@app.route("/")
def index():

    name = "David"
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 

    return render_template("index.html", name = name, numeros = numeros)#


#en el html
"""
    <ul>
        <!--asi imprimimos una lista desde python-->
        {%for numero in numeros%}
            <li> {{ numero }} </li> 
        {% endfor %}

    </ul>
"""










