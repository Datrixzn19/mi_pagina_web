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

#base.html
"""
<!--este el el archivo base, este hereda todo su contenido a los archivos que lo llamen con el extends-->

<!--en el archivo en el que estemos heredando todo lo que no este en un endblock no se renderizara y por lo tanto no se va a mostrar-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola {% block titulo%} {% endblock%} </title>
</head>
<body>
    <h1>Bienvenido {% block saludo%}
        <!--aqui va el contenido, lo podemos en el archivo que este heredando-->
    {% endblock%}</h1>
    
</body>
</html>
"""
#index.html
"""
<!--borramos lo de html body etc porque eso lo hereda de la plantilla-->
{%extends "base.html"%}<!--colocamos el nombre de la plantilla de la cual vamos a heredar--> 


    {% block titulo%} mundo {% endblock%}

    {% block saludo%} te damos la bienvenidaa la pagina principal 
    
    {% if name %}<!--esto dara true por lo que si se mostrara el nombre-->
        <h1>Bienvenido, {{ name }}</h1>
    {% else  %}
        <h1>Bienvenido, no tenemos tu nombre</h1>
    {% endif  %}<!--siempre debemos indicar en donde acaba el if porque sino da error-->


    <ul>
        <!--asi imprimimos una lista desde python-->
        {%for numero in numeros%}
            <li> {{ numero }} </li> 
        {% endfor %}

    </ul>


    <ul>{{numeros}}</ul><!--nose hice la prueba haber que hace, y los muestra asi [1,2,3...0]-->
    {% endblock%}

<h3>hola h3</h3><!--esto no se va a mostrar porque esta fuera de un block-->

"""