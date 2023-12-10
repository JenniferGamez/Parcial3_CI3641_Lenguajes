class Persona(val nombre: String, val edad: Int)

fun any() {
    val persona1 = Persona("Alice", 30)
    val persona2 = Persona("Alice", 30)

    println(persona1.equals(persona2)) // Compara referencias (por defecto)
    println(persona1.hashCode()) // Código hash
    println(persona1.toString()) // Representación de cadena
}

interface Volador {
    fun volar()
}

interface Nadador {
    fun nadar()
}

class Pato : Volador, Nadador {
    override fun volar() { /* Implementación */ }
    override fun nadar() { /* Implementación */ }
}

//Manejo de Varianzas

// Covarianza
interface Productor<out T> {
    fun producir(): T
}
fun imprimirLista(lista: List<out Any>) {
    // Código que lee elementos de la lista
}

// Contravarianza
interface Consumidor<in T> {
    fun consumir(item: T)
}
open class Animal
class Perro : Animal()

// Varianza
class Caja<T>(val elemento: T)

fun main(){
    any()

    // Herencia simple
    open class Animal
    class Perro : Animal()

    // Uso de la varianza
    
    // Covarianza
    val listaDeStrings: List<String> = listOf("A", "B", "C")
    imprimirLista(listaDeStrings) // Acepta List<Any> por covarianza
    val consumidorDeAnimal: Consumidor<Animal> = object : Consumidor<Animal> {
        override fun consumir(item: Animal) {
            println("Consumiendo animal")
        }
    }
    val consumidorDePerro: Consumidor<Perro> = object : Consumidor<Perro> {
        override fun consumir(item: Perro) {
            println("Consumiendo perro")
        }
    }
    val consumidorDeAnimalContravariante: Consumidor<in Perro> = consumidorDeAnimal

    consumidorDeAnimalContravariante.consumir(Perro()) // Acepta consumir un Perro


    // Varianza sin notacion, varianza
    val cajaDeEntero: Caja<Int> = Caja(42)
    val cajaDeAny: Caja<Any> = cajaDeEntero // Esto dará un error, ya que Caja es invariante

}
