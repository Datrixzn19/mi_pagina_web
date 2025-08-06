#creacion de formularios con WTForm
# Necesitamos instalar esta libreria, detenemos el server y escribimos pip install flask-wtf
#para crear estos formularios debemos crear una clave secreta --> app.config.from_mapping
#esta clave se la crea simpre que vayamos a trabajar con inicios de secion y otras cosas silimares, es obligatorio

from flask import Flask, render_template, url_for, request 

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'dev'
)



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









#Crear formularios con wtforms 
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField #estos son para craer inputs segun el tipo

class registerForm(FlaskForm):#debemos crear una clase y que herede FlaskForm

    username = StringField("Registrar usuario: ")
    password = PasswordField("Contraseña usuario: ")
    submit = SubmitField("Enviar")
    

#creamos una ruta para la pagina de registro
@app.route("/auth/register", methods = ['GET', 'POST'])#por defecto trabajo con get, pero podemos especificar que use post
def register():
    form  = registerForm()#hacemos la instancia 
    if form.validate_on_submit():
    #valida los datos y ejecuta esto en el metodo post, para que funcione debe estar en nuestro html
        username = form.username.data
        password = form.password.data
        return f"user {username} contra {password}"


    return render_template("auth/register.html", form = form)




    #forma anterior
    """
    if request.method == "POST":
        username = request.form['username']#dentro de la lista va el nombre del valor del atributo name en el input del form
        password = request.form['password']

        if len(username)>2 and len(password)>5:
            return f"user {username} contra {password}"
            
        else:
            error = "El nombre debe ser mayor a 3 dijtos y la contra mayor a 4"
            return render_template("auth/register.html",form = form, error = error)
            """
    
#en register.html
"""
    {%extends "base.html"%}<!--colocamos el nombre de la plantilla de la cual vamos a heredar--> 


    {% block titulo%} Registro {% endblock%}

    {% block saludo%}
        <h1>Pagina de registro</h1>
<!--Formulario anterior para probar las validaciones 
        <form action="" method="post"> comment:es una buena practica este metodo, porque sino al enviar los datos se muestran en la url, con post no pero debemos especificar en la vista que vamos a recibir datos en ese metodo

            <label for="username">Nombre de usuario</label>
            <input name="username" type="text" id=username">
            <br>
            <label for="password">Contraseña</label>
            <input name="password" type="password" id="password">
            <br>
            <button value="Register" type="submit">Enviar</button>
        </form> -->

        <form action="" method="post">
            {{ form.hidden_tag() }}
            {{ form.username.label }} {{ form.username }}
            {{ form.password.label }} {{ form.password }}
            {{ form.submit }}

        </form>


        {%if error%}
        <p style="color: red;"> {{error}} </p>
        
        {%endif%}

    {%endblock%}
"""