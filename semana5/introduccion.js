const form = document.querySelector('.formBuscador');
const inputUrl = document.getElementById('url');
const galeria = document.getElementById('contenedorGaleria');
let imagenSeleccionada = null;


// Manejar el envío del formulario
form.addEventListener('submit', function(e) {
    e.preventDefault(); // hacer que la pagina no se recargue
    
    const url = inputUrl.value.trim();
    
    if (url) {
        agregarImagen(url);
    }
});







function agregarImagen(url) {
    // un div para la imagen 
    const contenedor = document.createElement('div');
    contenedor.className = 'imagen-container';
    
    // Poner img
    const img = document.createElement('img');
    img.src = url; 
    img.alt = 'Imagen';
    
    // Borrar img
    const btnEliminar = document.createElement('button');
    btnEliminar.className = 'eliminar'; //para css
    btnEliminar.innerHTML = 'X';
    btnEliminar.title = 'Eliminar imagen';
    
    // Agregar evento de clic para eliminar
    btnEliminar.addEventListener('click', function() {
        contenedor.remove();
        if (imagenSeleccionada === contenedor) {
            imagenSeleccionada = null;
        }
    });
    


    // seleccion 
    contenedor.addEventListener('click', function() {
        // Quitar selección anterior en caso de que haya 
        if (imagenSeleccionada) {
            imagenSeleccionada.classList.remove('seleccionada');
        }
        
        // Seleccionar imagen  imagen
        contenedor.classList.add('seleccionada');
        imagenSeleccionada = contenedor;
        
    });
    

    
    contenedor.appendChild(img);//append child agrega como hijo 
    contenedor.appendChild(btnEliminar);
    
    // Agregarla ala galeria 
    galeria.appendChild(contenedor);
}



// Manejar evento de teclado para eliminar imagen seleccionada
document.addEventListener('keydown', function(e) {
    // En caso de que se precione la tecla Del
    if (e.key === 'Delete' && imagenSeleccionada) {
        imagenSeleccionada.remove();
        imagenSeleccionada = null;
    }
});




