//Validacion de formularios 

/*
REQUISITOS 
Nombre (mínimo 3 caracteres).
Correo electrónico (validar formato correcto).
Contraseña (mínimo 8 caracteres con al menos un número y un carácter especial).
Confirmación de contraseña (debe coincidir con la contraseña).
Edad (debe ser mayor o igual a 18 años).
*/

document.addEventListener("DOMContentLoaded", () => {//esperar a que cargue el DOM 
 
  let form = document.getElementById("form");
  let inputNombre = document.getElementById("inputNombre");
  let inputCorreo = document.getElementById("exampleInputEmail1");
  let inputContra = document.getElementById("exampleInputPassword")
  let inputContraRep = document.getElementById("exampleInputPassword2")
  let inputEdad = document.getElementById("edad")
  let confirmacionEntrada = document.getElementById("confirmar")

  form.addEventListener("input", e => {
    e.preventDefault();//evita que se recargue la pagina 
     let entrar = true;//para que se vuelva a poner a true en caso de ser necesario 
      //limpiar los erroes 
      document.getElementById("errorNombre").innerHTML = "";
      document.getElementById("errorCorreo").innerHTML = "";
      document.getElementById("errorContra").innerHTML = "";
      document.getElementById("errorContra1").innerHTML = "";
      document.getElementById("errorContraRep").innerHTML = "";
      document.getElementById("errorEdad").innerHTML = "";
 


   
    let emailRegExp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; //expresion regular para validar correos usar ente /regex/
    let contraRegExp = /[!@#$%^&*(),.?":{}|<>]/;
    
 

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
 

    if(inputContra.value.length<6){//para la primera contraseña
        document.getElementById("errorContra").innerHTML = `La contraseña es muy corta <br>`
        entrar = false
        document.getElementById("exampleInputPassword").style.border = "3px solid red"
    }else{
      document.getElementById("exampleInputPassword").style.border = "none"
    }


    if(!contraRegExp.test(inputContra.value)){//para que pida un caracter especial 
        document.getElementById("errorContra1").innerHTML = "Introduce al menos un caracter especial"
        entrar = false
        
    }


    if(inputContraRep.value!=inputContra.value){//confirmacion de la contraseña 
        document.getElementById("errorContraRep").innerHTML = "Las contraseñas no coinciden"
        entrar = false
        document.getElementById("exampleInputPassword2").style.border = "3px solid red"

    }else{
      document.getElementById("exampleInputPassword2").style.border = "none"


    }


    if(inputEdad.value <18 || inputEdad.value >64){
      document.getElementById("errorEdad").innerHTML =`<br>La edad debe ser de entre 18 y 64 años`
      entrar = false
      document.getElementById("edad").style.border = "3px solid red"
    }else{
      document.getElementById("edad").style.border = "none"
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
      confirmacionEntrada.style.display = "default"
      confirmacionEntrada.style.color = "rgb(17, 255, 0)";//mod estilos desde js 
      confirmacionEntrada.innerHTML = "El formulario se ha enviado correctamente"

      
    }else{
      confirmacionEntrada.style.display = "none"
      confirmacionEntrada.innerHTML = ""
    }


  })//cierre del submit 























});//cierre de esperar al dom