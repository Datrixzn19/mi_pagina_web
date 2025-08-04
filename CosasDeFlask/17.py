#formularios
#solo he puesto el bloque especifico faltan algunas cosas 
#creacion de la ruta para la pagina de registro

from flask import Flask, render_template, url_for, request #necesitamos el obj request para capturar la peticion del cliente, por ej lo que nos va a enviar con el form  

#creamos una ruta para la pagina de registro
@app.route("/auth/register", methods = ['GET', 'POST'])#por defecto trabajo con get, pero podemos especificar que use post
def register():
    if request.method == "POST":
        username = request.form['username']#dentro de la lista va el nombre del valor del atributo name en el input del form
        password = request.form['password']

        if len(username)<3 and len(password)<5:
            error = "El nombre debe ser mayor a 3 dijtos y la contra mayor a 4"
            return render_template("auth/register.html", error = error)
        else:
            return f"user {username} contra {password}"
            

    return render_template("auth/register.html")









#en register.html creamos un form normal 
"""
    {% block saludo%}
        <h1>Pagina de registro</h1>
        <form action="" method="post">

            <label for="username">Nombre de usuario</label>
            <input name="username" type="text" id=username">
            <br>
            <label for="password">Contraseña</label>
            <input name="password" type="password" id="password">
            <br>
            <button value="Register" type="submit">Enviar</button>

        </form>

        {%if error%}
        <p style="color: red;"> {{error}} </p>
        {%endif%}

    {%endblock%}
"""