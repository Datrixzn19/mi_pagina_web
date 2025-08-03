#renderizacion de plantillas

#creacion de funciones personalizadas y envio de datos a plantillas 

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



@app.route("/hello")#
@app.route("/hello/<string:name>")#
@app.route("/hello/<string:name>/<int:edad>")
@app.route("/hello/<string:name>/<int:edad>/<string:email>")
def hello(name = None, edad = None, email = None):
    myData = {
        "name": name,
        "edad": edad,
        "email": email
        }
    return render_template("hello.html", data = myData)




#en el index
"""
<!--borramos lo de html body etc porque eso lo hereda de la plantilla-->
{%extends "base.html"%}<!--colocamos el nombre de la plantilla de la cual vamos a heredar--> 


    {% block titulo%} mundo {% endblock%}

    {% block saludo%} te damos la bienvenidaa la pagina principal 
    
    {% if name %}<!--esto dara true por lo que si se mostrara el nombre-->
        <h1>Bienvenido, {{ name | upper }}</h1>
        <h1> {{ repeticion("cadenaRepetida", 3) }} </h1>
    {% else  %}
        <h1>Bienvenido, no tenemos tu nombre</h1>
    {% endif  %}<!--siempre debemos indicar en donde acaba el if porque sino da error-->


  


  
    {% endblock%}








"""
#en hello.html

"""
{%extends "base.html"%}<!--colocamos el nombre de la plantilla de la cual vamos a heredar--> 


    {% block titulo%} mundote desde hello.html{% endblock%}

    {% block saludo%} te damos la bienvenidaa hello.html 
    
    
    {% if data.name is none and data.edad is none: %} <!--en jinja es none con minuscula == = is-->
        <h1> No ha enviado valores</h1>
    {%elif edad is none%}
        <h1>Hola {{data.name}}, no has dado tu edad</h1> 
    {%else%}
        <h1>Hola {{data.name}}, tienes {{data.edad}} años</h1>   
    {% endif%}

  
    {% endblock%}
    
"""