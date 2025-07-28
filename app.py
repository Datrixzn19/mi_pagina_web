#ESCPAPE DE HTML 

#En flask se recomienda escapar todas las entradas, esto es para que no se pueda ingresar codigo por la ruta 
# 
from flask import Flask

app = Flask(__name__)#

@app.route("/")
def index():
    return "<h1>Ruta base!</h1>"



#Ejemplo sin escape 
@app.route("/codigo/<path:code>")#podrian inyectar codigo ej. http://127.0.0.1:5000/code2/<script>alert("hackeado")</script>
def a(code):
    return f"<code>{code}</code>"

#ejemplo con escape 
from markupsafe import escape#esto viene junto con flask 
@app.route("/codigo2/<path:code>")#aqui si ponene codigo lo mostrara como texto y no podran hacer inyecciones de codigo 
def b(code):
    return f"<code>{escape(code)}</code>"



