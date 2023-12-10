open class A {
    open fun saludar() {
        println("Hola desde A")
    }
}

class B : A() {
    override fun saludar() {
        println("Hola desde B")
    }
}

fun main() {
    val instanciaA: A = B()
    instanciaA.saludar() // Imprimirá "Hola desde B" debido al enlace estático
}
