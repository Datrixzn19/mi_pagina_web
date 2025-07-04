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
  let parrafowarnings = document.getElementById("warnings");

  form.addEventListener("submit", e => {
    e.preventDefault();
    let warnings = "";
    let entrar = false;

    if (inputNombre.value.length <= 6) {
      warnings += `Nombre muy corto <br>`;
      console.log("muy corto");
      entrar = true;
    }

    if (entrar) {
      parrafowarnings.innerHTML = warnings;
    } else {
      parrafowarnings.innerHTML = "Formulario enviado correctamente";
    }

































  });//cierre addevent





































});//cierre de esperar al dom
