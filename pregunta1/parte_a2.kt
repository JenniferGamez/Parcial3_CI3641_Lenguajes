import java.lang.ref.WeakReference

fun objInaccesible() {
    var a: String? = "Hola"
    println(a)

    a = null // La referencia 'a' ya no apunta al objeto
    // En este punto, el objeto "Hola" se vuelve inaccesible
    println(a) // Imprime null
}

fun referenciaDebil() {
    var b: WeakReference<String>? = WeakReference("Adiós") // Creamos un objeto String con referencia débil
    var otraReferencia = b

    println(b?.get())

    b = null // Eliminamos la referencia directa a través de la variable 'b'

    println(otraReferencia) // Imprime que java.lang.ref.WeakReference@3fee733d indicando la referencia débil

}

fun referenciaFuerte() {
    var c: String? = "Hola" // Creamos un objeto String
    val otraReferencia = c // Creamos otra referencia apuntando al mismo objeto

    println(c)
    println(otraReferencia)

    c = null // Se elimina una de las referencias directas
    // Aún existe otra referencia directa (otraReferencia) apuntando al objeto "Hola"

    // El objeto "Hola" no se elimina de la memoria porque todavía hay una referencia apuntando a él (otraReferencia)
    println(otraReferencia) // Imprime "Hola"
}

fun main(){
    objInaccesible()
    referenciaDebil()
    referenciaFuerte()
}