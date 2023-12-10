// Jennifer Gamez
// 16-10396

// PREGUNTA B

////////////////
// PARTE B.1
////////////////


import java.util.LinkedList
import java.util.Queue

// Interfaz abstracta Secuencia
interface Secuencia<T> {
    fun agregar(elemento: T)
    fun remover(): T
    fun vacio(): Boolean
}

// Implementación de Pila
class Pila<T> : Secuencia<T> {
    public val elementos = mutableListOf<T>()

    // Función que agrega un elemento a la pila
    override fun agregar(elemento: T) {
        elementos.add(elemento)
        //println("Se agregró con éxito a la pila el elemento ${elemento}")
    }

    // Función que elemento un elemento a la pila
    override fun remover(): T {
        if (vacio()) {
            throw NoSuchElementException("La pila está vacía")
        }
        //println("Se eliminó con éxito de la pila el elemento ${elementos.last()}")
        return elementos.removeAt(elementos.size - 1)
    }
    
    // Función que evalúa si la pila está vacía
    override fun vacio(): Boolean {
        return elementos.isEmpty()
    }

    // Función para mostrar los elementos de la pila
    fun mostrarPila() {
        println("Contenido de la pila: $elementos")
    }
}

// Implementación de Cola
class Cola<T> : Secuencia<T> {
    public val elementos: Queue<T> = LinkedList()

    // Función que agrega un elemento a la cola
    override fun agregar(elemento: T) {
        elementos.add(elemento)
        //println("Se agregó con éxito a la cola el elemento $elemento")
    }

    // Función que elimina un elemento a la cola
    override fun remover(): T {
        if (vacio()) {
            throw NoSuchElementException("La cola está vacía")
        }
        val elementoRemovido = elementos.remove()
        //println("Se eliminó con éxito de la cola el elemento $elementoRemovido")
        return elementoRemovido
    }

    // Función que evalúa si la cola está vacía
    override fun vacio(): Boolean {
        return elementos.isEmpty()
    }

    // Función para mostrar los elementos de la cola
    fun mostrarCola() {
        println("Contenido de la cola: $elementos")
    }
}

////////////////
// PARTE B.2
////////////////

// Definición del tipo de datos para representar grafos como listas de adyacencias
class Grafo {
    private val adyacencias: MutableMap<Int, MutableList<Int>> = mutableMapOf()

    fun agregarVertice(vertice: Int) {
        adyacencias[vertice] = mutableListOf()
    }

    fun agregarArista(origen: Int, destino: Int) {
        adyacencias[origen]?.add(destino)
    }

    fun obtenerAdyacencias(vertice: Int): List<Int>? {
        return adyacencias[vertice]
    }
}

// Clase abstracta Busqueda para búsqueda de nodos en un grafo
abstract class Busqueda {
    abstract fun buscar(grafo: Grafo, inicio: Int, objetivo: Int): Int
}

// Clase DFS que implementa la búsqueda a profundidad
class DFS : Busqueda() {
    override fun buscar(grafo: Grafo, inicio: Int, objetivo: Int): Int {
        val visitados = mutableSetOf<Int>()
        val pila = Pila<Int>()
        var nodosExplorados = 0

        pila.agregar(inicio)

        while (!pila.vacio()) {
            val actual = pila.remover()

            if (actual == objetivo) {
                return nodosExplorados
            }

            if (actual !in visitados) {
                visitados.add(actual)
                nodosExplorados++

                grafo.obtenerAdyacencias(actual)?.reversed()?.forEach {
                    if (it !in visitados) {
                        pila.agregar(it)
                    }
                }
            }
        }

        return -1
    }
}

// Clase BFS que implementa la búsqueda a amplitud
class BFS : Busqueda() {
    override fun buscar(grafo: Grafo, inicio: Int, objetivo: Int): Int {
        val visitados = mutableSetOf<Int>()
        val cola = Cola<Int>()
        var nodosExplorados = 0

        cola.agregar(inicio)

        while (!cola.vacio()) {
            val actual = cola.remover()

            if (actual == objetivo) {
                return nodosExplorados
            }

            if (actual !in visitados) {
                visitados.add(actual)
                nodosExplorados++

                grafo.obtenerAdyacencias(actual)?.forEach {
                    if (it !in visitados) {
                        cola.agregar(it)
                    }
                }
            }
        }

        return -1
    }
}

fun main() {
    val grafo = Grafo()
    grafo.agregarVertice(0)
    grafo.agregarVertice(1)
    grafo.agregarVertice(2)
    grafo.agregarVertice(3)
    grafo.agregarVertice(4)
    grafo.agregarArista(0, 1)
    grafo.agregarArista(0, 2)
    grafo.agregarArista(3, 2)
    grafo.agregarArista(1, 4)


    val busquedaDFS = DFS()
    val resultadoDFS = busquedaDFS.buscar(grafo, 0, 4)
    println("DFS - Nodos explorados: $resultadoDFS")

    val busquedaBFS = BFS()
    val resultadoBFS = busquedaBFS.buscar(grafo, 0, 3)
    println("BFS - Nodos explorados: $resultadoBFS")
}