from gestorclase import *

tablaMetodoVirt = GestorTablasMetodoVirtual()

# Programa es el programa principal que llama las implementaciones para hacer uso de las tablas de métodos virtuales. de gestorclase.py

def programa():

    print("Manejador de tablas de métodos virtuales para un sistema orientado a objetos con herencia simple y despacho dinámico de métodos")
    print("Ingrese una acción (CLASS <tipo> [<nombre>], DESCRIBIR <nombre>, SALIR)")

    salir = False  # Controlar la salida del bucle

    while not salir:

        linea = input("> ")
        instruccion = linea.strip().split()

        if instruccion:
            if instruccion[0].upper() == "CLASS":
                print(tablaMetodoVirt.definir_tabla(instruccion[1:]))

            elif instruccion[0].upper() == "DESCRIBIR":
                print(tablaMetodoVirt.describir_clase(instruccion[1:]))

            elif instruccion[0].upper() == "SALIR":
                salir = True

            else:
                print("   La  acción debe ser (CLASS <tipo> [<nombre>], DESCRIBIR <nombre>, SALIR)")
        else:
            print("   Debe ingresar una opción válida.")
    
    
# Ejecutar el bucle principal
if __name__ == "__main__":
    programa()