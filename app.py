#validaciones con wtforms 

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









#validar formularios con wtforms 
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField 
from wtforms.validators import DataRequired, length #para decir requerido y para cuantos caracteres 
class registerForm(FlaskForm):

    username = StringField("Registrar usuario: ", validators=[DataRequired(),  length(min=3, max=25)]) 
    password = PasswordField("Contraseña usuario: ", validators=[DataRequired(), length(min=4, max=25)])
    submit = SubmitField("Enviar")
    


@app.route("/auth/register", methods = ['GET', 'POST'])
def register():
    form  = registerForm()#hacemos la instancia 
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"user {username} contra {password}"


    return render_template("auth/register.html", form = form)
