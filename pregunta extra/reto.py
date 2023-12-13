import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n) / math.sqrt(5))

def wadef_oc(n):
    if n <= 1:
        return 1

    result = 2 << n // (n - 1)  # Equivalente a 2**(n+1) // (n-1)
    fib_index = result.bit_length() + 1  # Obtener el índice para la función de Fibonacci
    return fibonacci(fib_index)

if __name__ == "__main__":
    n = int(input("Ingrese el valor de n: "))
    resultado = wadef_oc(n)
    print(f"El valor de wadef_oc({n}) es: {resultado}")
