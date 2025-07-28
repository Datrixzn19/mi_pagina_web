#Rutas, escape de etiquetas, dos rutas para una vista 


from flask import Flask

app = Flask(__name__)#este name indica que este archivo es el principal 

#podemos tener varias rutas, pero no se pueden repetirel nombre(solo mostrara la primera) ni el nombre de la funcion tampoco

@app.route("/")#podemos tener dos rutas para una sola vista(la funcion)
@app.route("/index")
def index():
    return "<h1>Ruta base!</h1>"#podemos DEVOLVER ETIQUETAS HTML 


@app.route("/hello")#este slash indica la ruta base cada, se accede con ip/hello por ejemplo en este caso
def hello():
    return "Hello, world!"#devolviendo solo texto plano  sin etiquetas 


