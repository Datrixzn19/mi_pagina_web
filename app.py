#Formularios

#Manejo de formularios 
#creacion de la ruta para la pagina de registro
from flask import Flask, render_template, url_for
 

app = Flask(__name__)




@app.route("/")
def index():
    print(url_for("index", name = "davdfsfdsfid", edad = 20))
    print(url_for("hello")) 
    name = None
    edad = None
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return render_template("index.html",
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


#creamos una ruta para la pagina de registro
@app.route("/auth/register")
def register():
    return render_template("auth/register.html")