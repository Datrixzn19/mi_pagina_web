//Sintaxis basica de javascript

// ================ VARIABLES ================
let variableModificable = "puede cambiar";
const CONSTANTE = "valor fijo";
var variableAntigua = "no recomendada";

// ================ TIPOS DE DATOS ================
// Primitivos
let string = "texto";
let number = 42;
let boolean = true;
let nulo = null;
let indefinido;
let simbolo = Symbol("id");
let bigInt = 9007199254740991n;

// Objetos
let objeto = { 
  clave: "valor",
  metodo: function() { return this.clave; }
};
let array = [1, "dos", false];
let fecha = new Date();

// ================ OPERADORES ================
// Aritméticos
let suma = 10 + 5;      // 15
let resta = 10 - 5;     // 5
let multiplicacion = 10 * 5; // 50
let division = 10 / 5;  // 2
let modulo = 10 % 3;    // 1
let exponente = 2 ** 3; // 8

// Comparación
console.log(5 == "5");   // true (igualdad)
console.log(5 === "5");  // false (igualdad estricta)
console.log(5 != "5");   // false
console.log(5 !== "5");  // true
console.log(5 > 3);      // true
console.log(5 <= 5);     // true

// Lógicos
console.log(true && false); // false (AND)
console.log(true || false); // true (OR)
console.log(!true);         // false (NOT)

// Asignación
let x = 10;
x += 5;  // x = 15
x *= 2;  // x = 30

// ================ ESTRUCTURAS DE CONTROL ================
// If-else
if (x > 20) {
  console.log("x es mayor que 20");
} else if (x === 20) {
  console.log("x es 20");
} else {
  console.log("x es menor que 20");
}

// Operador ternario
let resultado = (x >= 30) ? "Mayor o igual" : "Menor";

// Switch
switch (new Date().getDay()) {
  case 0: console.log("Domingo"); break;
  case 1: console.log("Lunes"); break;
  default: console.log("Otro día");
}

// Bucles
// For
for (let i = 0; i < 5; i++) {
  console.log(i); // 0,1,2,3,4
}

// While
let j = 0;
while (j < 3) {
  console.log(j); // 0,1,2
  j++;
}

// Do-while
let k = 0;
do {
  console.log(k); // 0 (siempre se ejecuta al menos una vez)
  k++;
} while (k < 1);

// ================ FUNCIONES ================
// Declaración
function sumar(a, b) {
  return a + b;
}

// Expresión
const restar = function(a, b) { return a - b; };

// Arrow function (ES6+)
const multiplicar = (a, b) => a * b;

// Parámetros por defecto
function saludar(nombre = "Usuario") {
  return `Hola, ${nombre}`;
}

// ================ OBJETOS Y CLASES ================
// Objeto literal
let persona = {
  nombre: "Ana",
  edad: 25,
  saludar: function() {
    return `Hola, soy ${this.nombre}`;
  }
};

// Clases (ES6)
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  saludar() {
    return `Hola, soy ${this.nombre}`;
  }
}

const ana = new Persona("Ana", 25);

// ================ ARRAYS Y MÉTODOS ================
let numeros = [1, 2, 3, 4, 5];

// Métodos comunes
numeros.push(6);        // Añade al final
numeros.pop();          // Elimina el último
numeros.unshift(0);     // Añade al inicio
numeros.shift();        // Elimina el primero
numeros.includes(3);    // true
numeros.indexOf(4);     // 3
numeros.slice(1, 3);    // [2, 3] (subarray)
numeros.map(n => n * 2); // [2, 4, 6, 8, 10]
numeros.filter(n => n > 3); // [4, 5]

// ================ MANEJO DE ERRORES ================
try {
  // Código que puede fallar
  let dato = JSON.parse("texto no válido");
} catch (error) {
  console.error("Error:", error.message);
} finally {
  console.log("Siempre se ejecuta");
}

// ================ PROMESAS Y ASYNC/AWAIT ================
// Promesa
const promesa = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Éxito"), 1000);
});

promesa
  .then(res => console.log(res))
  .catch(err => console.error(err));

// Async/Await
async function obtenerDatos() {
  try {
    const respuesta = await fetch("https://api.example.com");
    const datos = await respuesta.json();
    console.log(datos);
  } catch (error) {
    console.error("Error al obtener datos:", error);
  }
}

// ================ MÓDULOS (ES6) ================
// Exportar (en archivo 'modulo.js')
// export const PI = 3.1416;
// export function suma(a, b) { return a + b; }

// Importar (en otro archivo)
// import { PI, suma } from './modulo.js';