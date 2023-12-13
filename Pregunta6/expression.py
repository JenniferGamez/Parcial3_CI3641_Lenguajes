# Jennifer Gamez
# 1610396

import re

# Parte a. Expresiones
# Manejador de expresiones

class Expression:
    def __init__(self, exp_str):
        self.exp_str = exp_str.strip()
        self.type = self.detect_type()

    def detect_type(self):
        # Identifica si la expresión es un atomo
        if re.match(r'^[a-z][a-zA-Z0-9_]*$', self.exp_str): # minusculas
            return "Atomo"
        # Identifica si la expresión es una variable
        elif re.match(r'^[A-Z][a-zA-Z0-9_]*$', self.exp_str): # masyusculas
            return "Variable"
        # Identifica si la expresión es una estrcutura
        elif re.match(r'^[a-z][a-zA-Z0-9_]*\((.*)\)$', self.exp_str): # hay comas
            return "Estructura"
        else:
            return "Expresión no conocida."