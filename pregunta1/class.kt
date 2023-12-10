// Clase pública
class ClasePublica {
    // Accesible en cualquier parte
    // Propiedades y métodos son públicos por defecto
    val propiedadPublica = "Esta es una propiedad pública"
    fun funcionPublica() {
        println("Esta es una función pública")
    }
}

// Clase privada
class ClasePrivada {
    // Accesible solo en el alcance actual
    private val propiedadPrivada = "Esta es una propiedad privada"
    private fun funcionPrivada() {
        println("Esta es una función privada")
    }
}

// propiedadProtegida es accesible en la clase ClaseProtegida y también en su subclase ClaseHija.
open class ClaseProtegida {
    // Accesible en la clase actual y en sus subclases
    protected val propiedadProtegida = "Esta es una propiedad protegida"
}

class ClaseHija : ClaseProtegida() {
    fun accederPropiedadProtegida() {
        println("El valor de propiedadProtegida es $propiedadProtegida")
    }
}

// Clase protegida
internal class ClaseInterna {
    // Accesible dentro del mismo módulo
    internal val propiedadInterna = "Esta es una propiedad interna"
    internal fun funcionInterna() {
        println("Esta es una función interna")
    }
}

// Clase con constructor primario
class PersonaPrim(val nombre: String, var edad: Int) {}

// Constructor secundario
class Persona {
    var nombre: String = ""
    var edad: Int = 0
    
    constructor(nombre: String, edad: Int) {
        // Campos (Atributos), pueden ser mutables o inmmutables
        val nombre: String = "Sin nombre" // Propiedad inmutable
        var edad: Int = 0 // Propiedad mutable
    }

    fun saludar() { // Método de la clase
        println("¡Hola, soy $nombre y tengo $edad años!")
    }
}

// tipo generico 

// Clase generica, puede contener cualquier tipo de dato
class Contenedor<T>(var valor: T) {
    fun obtenerValor(): T { 
        return valor
    }
}

// Se crea instancias 
val contenedorInt = Contenedor(5) // contenedor de tipo int
val contenedorStr = Contenedor("Hola") // contenedor de tipo string

// obtener valor de acuerdo a su tipo
val valorInt: Int = contenedorInt.obtenerValor() 
val valorStr: String = contenedorStr.obtenerValor()

// Ejemplo de error al instanciar la clase

class PersonaTipo<T>(var carnet: Int)

val estudianteInt = PersonaTipo<Int>(1610396)
//val estudianteOtro = PersonaTipo<String>("Jennifer") // error se espera de tipo INT

// funcion generica que puede imprimir cualquier lista independiente del tipo de elemnto que contenga.
fun <T> imprimirLista(lista: List<T>) {
    for (elemento in lista) {
        println(elemento)
    }
}

fun listIndTipos(){ // Se imprime en main mas adelante
    val listaEnteros = listOf(1, 2, 3)
    val listaStrings = listOf("A", "B", "C")
    
    imprimirLista(listaEnteros)
    imprimirLista(listaStrings)
}

// convenciones de tipo

// convencion E
class ContenedorElemento<E>(val elemento: E)

// convencion K y V
class Diccionario<K, V>(val clave: K, val valor: V)

// Clase abstracta
abstract class Animal {
    abstract fun hacerSonido()
}

// Interfaz
interface Movimiento {
    fun moverse()
}

class Perro : Animal(), Movimiento {
    override fun hacerSonido() {
        println("Guau guau")
    }

    override fun moverse() {
        println("El perro se está moviendo")
    }
}

//instancia de perro y llamar a sus métodos
fun main() {
    // LIsta de tipo independiente
    listIndTipos()

    val miPerro = Perro()
    miPerro.hacerSonido() // Imprime "Guau guau"
    miPerro.moverse() // Imprime "El perro se está moviendo"
}