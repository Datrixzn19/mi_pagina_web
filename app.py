#renderizacion de plantillas

#uso de mas variables y datos 

from flask import Flask, render_template

app = Flask(__name__)#

@app.route("/")
def index():

    name = "David"

    return render_template("index.html", name = name)#














