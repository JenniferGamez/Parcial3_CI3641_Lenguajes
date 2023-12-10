from main import *
from gestorclase import *

import unittest
from io import StringIO
from unittest.mock import patch

class TestClase(unittest.TestCase):
    def test_constructor(self):
        # Prueba del constructor de la clase Clase
        clase = Clase('A', ['f', 'g'])
        self.assertEqual(clase.nombre_clase, 'A')
        self.assertEqual(clase.metodos, {'f': 'A', 'g': 'A'})
        self.assertIsNone(clase.super_clase)

    def test_herencia(self):
        # Prueba de herencia en la clase Clase
        super_clase = Clase('Super', ['h'])
        clase = Clase('A', ['f', 'g'], super_clase)
        self.assertEqual(clase.metodos, {'h': 'Super', 'f': 'A', 'g': 'A'})

class TestGestorTablasMetodoVirtual(unittest.TestCase):
    def setUp(self):
        self.tablaMetodoVirt = GestorTablasMetodoVirtual()

    def test_definir_tabla_sin_herencia(self):
        result = self.tablaMetodoVirt.definir_tabla(['A', 'f', 'g'])
        self.assertEqual(result, "   Nueva clase A definida con los metodos {'f': 'A', 'g': 'A'}")

    def test_definir_tabla_con_herencia(self):
        self.tablaMetodoVirt.definir_tabla(['A', 'f', 'g'])
        result = self.tablaMetodoVirt.definir_tabla(['B', ':', 'A', 'h'])
        self.assertEqual(result, "   Nueva clase B definida con los metodos {'f': 'A', 'g': 'A', 'h': 'B'}")

    def test_definir_tabla_clase_existente(self):
        self.tablaMetodoVirt.definir_tabla(['A', 'f', 'g'])
        result = self.tablaMetodoVirt.definir_tabla(['A', 'x', 'y'])
        self.assertEqual(result, "   ERROR: La clase 'A' ya existe")

    # Otros casos de prueba para definir_tabla

    def test_describir_clase_existente(self):
        self.tablaMetodoVirt.definir_tabla(['A', 'f', 'g'])
        result = self.tablaMetodoVirt.describir_clase(['A'])
        self.assertEqual(result, "f -> A :: f\ng -> A :: g")

    def test_describir_clase_inexistente(self):
        result = self.tablaMetodoVirt.describir_clase(['B'])
        self.assertEqual(result, "   ERROR: La clase 'B' no existe")



if __name__ == '__main__':
    unittest.main()
