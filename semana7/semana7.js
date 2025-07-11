const productos = [
    {nombre:"Lenovo Slim 7i", precio:"$899",descripcion:"Portatil de ultima generacion para ingenieria"},
    {nombre:"Logitech G502 ", precio:"$32",descripcion:"Mouse ergonomico inalambrico preciso para juegos"},
    {nombre:"Machenike k500", precio:"$32",descripcion:"Teclado mecanico 75%, cableado, ergonomico y de alta duracion"},
    {nombre:"Xiaomi buds 5", precio:"$21",descripcion:"Audifonos ergonomicos, inalambricos y con baja latencia"},
    {nombre:"Asus Rog Strix G16", precio:"$1800",descripcion:"Portatil muy potente para juegos"},
    {nombre:"Samsung S24 Ultra", precio:"$890",descripcion:"Telefono inteligente moderno, con camara de alta calidad y buen procesamiento"},
    {nombre:"LG UltraFine 4K", precio:"$650",descripcion:"Monitor 27 pulgadas de alta calidad y delgado"},
    {nombre:"WD Black SN850X", precio:"$120",descripcion:"SSD de 1TB, alta velocidad para gaming y trabajo"},
    {nombre:"Corsair Harpoon", precio:"$25",descripcion:"Mouse gaming ligero con sensor preciso de 12,000 DPI"},
    {nombre:"HyperX Cloud II", precio:"$80",descripcion:"Audifonos gaming con sonido envolvente y microfono removible"}
];
const lista = document.getElementById("listaProductos")
const botonAgg = document.getElementById("agregar")

//funciona para renderizar 
function renderizar(){
    lista.innerHTML = ""; //limpia la lista antes de renderizar porque sino se carga de nuevo toda la lista
    productos.forEach(productos => {//recorre cada uno en la lista 
        const item = document.createElement("li");//li por que estoy creando items 
        item.textContent = `Nombre del producto: ${productos.nombre} - Precio: ${productos.precio} - Descripcion: ${productos.descripcion}`;
        lista.appendChild(item)//agrega cada item a la lista 
    });
}


botonAgg.addEventListener("click", ()=>{
    console.log("Agregando producto...");
    const nuevoProducto = {
        nombre: "Cubot max 5",
        precio:"$200",
        descripcion:"Celular gamer accesible"
    };

    productos.push(nuevoProducto);
    renderizar();

});

window.onload=renderizar;