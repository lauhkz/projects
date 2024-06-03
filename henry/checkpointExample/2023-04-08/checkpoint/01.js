const Queue = require('../DS').Queue;

/* ⚠️ NO MODIFICAR NADA POR ENCIMA DE ESTA LÍNEA ⚠️

 ----*** 🍹 BAR CHECKPOINT 🍹 ***----

Felicitaciones por llegar a esta instancia! El checkpoint que realizarás a continuación
consistirá en resolver varios problemas que surgieron en un bar.
Tendrás que resolver cada uno de ellos, aplicando los conceptos aprendidos durante el módulo uno.
🍀 ¡Suerte! 🍀


1️⃣ ***** EJERCICIO 1 QUEUE ***** - guardarTragos() 1️⃣

Ha llegado un nuevo pedido de tragos. Es necesario recogerlos a todos y guardarlos dentro de la barra.
Además, se desea llevar un registro de la cantidad de cada trago que se ha vendido.Para esto tendrás que 
implementar la función guardarTragos, la cuál recibirá por parámetros una Queue con muchos 🍸 Tragos 🍸
que se tendrán que guardar en un objeto que nos servirá como contenedor.

📝 EJEMPLO 📝
(INPUT) ➡
["margarita", "daiquiri", "mojito", "piña colada", "negroni", "daiquiri"]

(OUTPUT) ➡
{
  margarita: {trago: "margarita", cantidad: 1},
  daiquiri: {trago: "daiquiri", cantidad: 2},
  mojito: {trago: "mojito", cantidad: 1},
  piña colada: {trago: "piña colada", cantidad: 1},
  negroni: {trago: "negroni", cantidad: 1}
}

REQUISITOS:
  🟢 Respetar el principio de FIFO que corresponde a las Queues a la hora de guardar los tragos.
  🟢 Retornar un objeto, que tendrá como key value los elementos que agregas y quitas de la Queue.
  🟢 Cada trago debe tener:
    - una propiedad "trago" que almacene el nombre del trago.
    - una propiedad "cantidad" que almacene la cantidad vendida del mismo.
  🟢 ¡SI O SI necesitás utilizar una Queue!

  👀 TIP: Chequear el archivo DS.js para ver la función constructora Queue, y ver sus métodos disponibles.
*/
/*
      margarita: { trago: "margarita", cantidad: 1 },
      daiquiri: { trago: "daiquiri", cantidad: 1 },
      mojito: { trago: "mojito", cantidad: 1 },
      "piña colada": { trago: "piña colada", cantidad: 1 },
      "negroni": { trago: "negroni", cantidad: 1 },
*/
  //   let node = new Node(valor); //{data:valor , next:null}
  //   let current = this.head; // parate en el primer elemento
  //   console.log("%cAgregando el nodo:", "color: cyan", node);
  //   if (!current) {
  //     // si la listya esta vacia
  //     this.head = node;
  //   } else {
  //     while (current.next) {
  //       // mientras que no encuente el ultimo valor
  //       current = current.next; // avanzo un paso
  //     }
  //     current.next = node;
  //     console.log("%cAhora yo soy el ultimo Nodo", "color:magenta", node);
  //   }
  //   this._length++;
  //   return node;
  // };
 class Node {
  constructor(data){
    this.data = data
    this.next = null
  }
 }
 function Queue(){
  this.queue = []
  this.head = null
 }

 Queue.prototype.add = function(value){
  let node = new Node(value)
  let current = this.head
  if(!current){
    this.head = node 
  }else{
    while(current.next){
      current.current.next
    }
    current.next = node
  }
  return node
 }

 Queue.prototype.remove = function(){
  return this.queue.shift()
 }

 Queue.prototype.size = function(){
  return this.queue.length()
 }

function guardarTragos() {
  // Tu código aquí:
 let obj = {} 
 let newQueue = new Queue()
}

// ⚠️ NO MODIFICAR NADA POR DEBAJO DE ESTA LÍNEA ⚠️
module.exports = guardarTragos;
