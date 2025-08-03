#Enlaces y rutas 

#para esto usamos la lib url_for


from flask import Flask, render_template, url_for
 

app = Flask(__name__)




@app.route("/")
def index():
    print(url_for("index", name = "davdfsfdsfid", edad = 20))#crea la ruta de la funcion index
    print(url_for("hello"))#aqui nos dira que no hemos enviado valores 
    name = None
    edad = None
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#lista que vamos a imprimir 
    return render_template("index.html",#podemos organizar si son muchas variables
                             name = name,
                             edad = edad,
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




#base
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
    <!--esto va fuera de content por lo tanto la heredaran los demas -->
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Inicio</a></li><!--ese index es el nombre de la vista-->
            <li><a href="{{ url_for('hello') }}">hello</a></li>
        </ul>
    </nav>

    <h1>Bienvenido {% block saludo%}
    {% endblock%}</h1>


    
</body>
</html>
"""
#index
"""
{%extends "base.html"%}<!--colocamos el nombre de la plantilla de la cual vamos a heredar--> 


    {% block titulo%} mundo {% endblock%}

    {% block saludo%} te damos la bienvenidaa la pagina principal 
    
    
        <h1>Bienvenido, {{ name }}</h1>
        <h1> {{edad}} </h1>

  


  


  
    {% endblock%}
"""
#pd: esto no me funciono lo de mandar valores pero buehhh