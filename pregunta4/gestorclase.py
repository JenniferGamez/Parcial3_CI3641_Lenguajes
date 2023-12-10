# Clase que define una clase con métido que puede tener métodos porpios y heredar métodos de una super clase padre.
class Clase:
    def __init__(self, nombre_clase: str, metodos_clase: list, super_clase=None):
        self.nombre_clase = nombre_clase
        self.super_clase = super_clase
        self.metodos = {} # Metodos es un diccionario con la unión de los métodos iniciales con los métodoso de la super clase

        if isinstance(super_clase, Clase):
            self.metodos = super_clase.metodos.copy() # Heredar métidos de la clase padre

        for metodo in metodos_clase:
            self.metodos[metodo] = nombre_clase

# Clase que implementa el manejador de tablas de métodos virtuales
class GestorTablasMetodoVirtual:
    def __init__(self) -> None:
        self.tabla = {}

    def definir_tabla(self, accion: list) -> str:
        nombre_clase_hija = accion[0]

        if nombre_clase_hija in self.tabla:
            return f"   ERROR: La clase '{nombre_clase_hija}' ya existe"
        
        # Si accion[1] == ":" tiene herencia de la clase 
        if accion[1] == ":":

            clase_padre = accion[2]

            if clase_padre not in self.tabla:
                return f"   ERROR: La clase padre '{clase_padre}' no existe"

            clase_padre_objeto = self.tabla[clase_padre]
            metodosnombre_clase_hija = accion[3:]

        # Si accion[1] != ":" no tiene herencia
        else:
            clase_padre_objeto = None
            metodosnombre_clase_hija = accion[1:]

        listTemp = [x for x in metodosnombre_clase_hija if metodosnombre_clase_hija.count(x) <= 1]

        if len(listTemp) < len(metodosnombre_clase_hija):
            return f"   ERROR: Hay métodos repetidos."

        # Creamos una nueva clase hija
        nueva_clase = Clase(nombre_clase_hija, metodosnombre_clase_hija, clase_padre_objeto)

        # Guardamos la clase hija nueva en la tabla
        self.tabla[nombre_clase_hija] = nueva_clase

        return f"   Nueva clase {nombre_clase_hija} definida con los metodos {nueva_clase.metodos}"

        
    def describir_clase(self, accion: str) -> str:

        if accion[0] not in self.tabla:
            return f"   ERROR: La clase '{accion[0]}' no existe"

        clase = self.tabla[accion[0]]
        metodosClase = clase.metodos.copy()

        respuesta = '\n'.join([f'{metodo} -> {metodosClase[metodo]} :: {metodo}' for metodo in metodosClase.keys()])

        return respuesta