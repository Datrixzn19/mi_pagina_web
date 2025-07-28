#renderizacion de plantillas

#uso de estructuras de control en html
#se usa en html esto: {{% %}}

from flask import Flask, render_template

app = Flask(__name__)#

@app.route("/")
def index():

    name = "David"

    return render_template("index.html", name = name)#en este caso si esta llegando nuestra var9iable, pero puede que en algun otro ejercicio no, por ello ponemos poner estructuras de control en html






#En nuestro HTML seria asi:
"""

    {% if name %}<!--esto dara true por lo que si se mostrara el nombre-->
        <h1>Bienvenido, {{ name }}</h1>
    {% else  %}
        <h1>Bienvenido, no tenemos tu nombre</h1>
    {% endif  %}<!--siempre debemos indicar en donde acaba el if porque sino da error-->


"""




