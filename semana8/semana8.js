//Validacion de formularios 

/*
REQUISITOS 
Nombre (mínimo 3 caracteres).
Correo electrónico (validar formato correcto).

*/

document.addEventListener("DOMContentLoaded", () => {//esperar a que cargue el DOM 
 
  let form = document.getElementById("form");
  let inputNombre = document.getElementById("inputNombre");
  let inputCorreo = document.getElementById("exampleInputEmail1");



  let confirmacionEntrada = document.getElementById("confirmar")

  form.addEventListener("input", e => {
    e.preventDefault();//evita que se recargue la pagina(se supone que para input no es necesario porque el no recarga la pagina)
     let entrar = true;//para que se vuelva a poner a true en caso de ser necesario 

      //limpiar los erroes, osea los campos span para nombre y correo
      document.getElementById("errorNombre").innerHTML = "";
      document.getElementById("errorCorreo").innerHTML = "";
    

    let emailRegExp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; //expresion regular para validar correos usar ente /regex/


    if (inputNombre.value.length < 3) {//para el NOMBRE 
    
      document.getElementById("errorNombre").innerHTML = "El nombre es demasiado corto"
      entrar = false
      document.getElementById("inputNombre").style.border = "3px solid red"

    }else{
      document.getElementById("inputNombre").style.border = "none"

    }
    
    if(!emailRegExp.test(inputCorreo.value)){//para el correo
        document.getElementById("errorCorreo").innerHTML = "El correo no es válido"
        entrar = false 
        document.getElementById("exampleInputEmail1").style.border = "3px solid red"
    }else{
      document.getElementById("exampleInputEmail1").style.border = "none"

    }
 

    if (entrar) {//habilitar boton 
      document.getElementById("boton-registro").disabled = false//quita el disable que puse en html
      
    }else{
      
      document.getElementById("boton-registro").disabled = true//continua desabilitado(por si lleno todos los campos y luego borro alguno)
      confirmacionEntrada.innerHTML = ""

    }





  });//cierre addevent


  form.addEventListener("submit", e =>{//se permitira el evento submit solo cuando todos los campos sean correctos 
     e.preventDefault();//evita que se recargue la pagina
     let entrar = true;


    if (entrar) {
      confirmacionEntrada.style.display = "block"
      confirmacionEntrada.style.color = "rgb(17, 255, 0)";//mod estilos desde js 
      confirmacionEntrada.innerHTML = "El formulario se ha enviado correctamente"

      setTimeout(function () { // esto para que me muestre el span de confirmacion antes de la alerta 
        alert("El formulario se envió correctamente");
      }, 50);//estos son milisegundos 

      
    }else{
      confirmacionEntrada.innerHTML = ""
    }


  })//cierre del submit 

});//cierre de esperar al dom