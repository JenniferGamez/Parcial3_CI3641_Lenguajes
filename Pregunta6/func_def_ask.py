# Jennifer Gamez
# 1610396

# Parte a. Expresiones
# Manejador de expresiones

from expression import *
import re

# Parte b
class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class Fact:
    def __init__(self, predicate_name, args):
        self.predicate_name = predicate_name
        self.args = args

class Rule:
    def __init__(self, predicate_name, args, *antecedents):
        self.predicate_name = predicate_name
        self.args = args
        self.antecedents = list(antecedents)

class KnowledgeBase:
    def __init__(self):
        self.facts = []  # Almacena los hechos
        self.rules = []  # Almacena las reglas

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)
        

# Parte b.i DEF Define un nuevo hecho o regla 
def process_def(expressions, base):
    if len(expressions) == 1:
        # Verificar si es un hecho
        match = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', expressions[0])
        if match:
            predicate_name, args = match.groups()

            # Eliminar espacios adicionales en la expresión
            args = args.replace(" ", "")

            # Crear un objeto de hecho
            fact = Fact(predicate_name, args.split(','))

            # Agregar el hecho a la base de conocimientos
            base.add_fact(fact)

            print(f"Se definió el hecho '{predicate_name}({args})'")
        else:
            print("Error: La expresión no está bien formada para definir un hecho")
    else:
        # Verificar si es una regla
        match = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', expressions[0])
        if match:
            predicate_name, args = match.groups()
            antecedents = expressions[1:]
            antecedents_str = ", ".join([ant.strip() for ant in antecedents])

            # Eliminar espacios adicionales en la expresión
            args = args.replace(" ", "")

            # Crear un objeto de regla
            rule = Rule(predicate_name, args.split(','), *antecedents)
    
            # Agregar la regla a la base de conocimientos
            base.add_rule(rule)

            print(f"Se definió la regla '{predicate_name}({args}) :- {antecedents_str}'")
        else:
            print("Error: La expresión no está bien formada para definir una regla")


def process_ask(expression, knowledge_base):

    match = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', expression)

    if match:
        predicate_name, args = match.groups()
        predicate = Predicate(predicate_name, args.split(','))
        
        # Verificar si la expresión está bien formada para una consulta
        if not args or any(not re.match(r'^[a-zA-Z]\w*$', arg.strip()) for arg in args.split(',')):
            print("Error: La expresión no está bien formada para una consulta")
            return
        
        found_match = False
        unifications = []

        for fact in knowledge_base.facts:
            if fact.predicate_name == predicate_name:
                if len(fact.args) == len(predicate.args):
                    unification = {}
                    for i, arg in enumerate(fact.args):
                        if arg[0].isupper():
                            if arg not in unification:
                                unification[arg] = predicate.args[i]
                            elif unification[arg] != predicate.args[i]:
                                break
                    else:
                        unifications.append(unification)
                        found_match = True

        for rule in knowledge_base.rules:
            if rule.predicate_name == predicate_name:
                unification = {}
                antecedents_match = True

                # Verificar si los antecedentes de la regla coinciden con los hechos
                for antecedent in rule.antecedents:
                    antecedent_predicate, antecedent_args = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', antecedent).groups()
                    antecedent_predicate = antecedent_predicate.strip()
                    antecedent_args = antecedent_args.split(',')

                    found = False

                    for fact in knowledge_base.facts:
                        if fact.predicate_name == antecedent_predicate:
                            if len(fact.args) == len(antecedent_args):
                                antecedent_unification = {}
                                for i, arg in enumerate(fact.args):
                                    if arg[0].isupper():
                                        if arg not in antecedent_unification:
                                            antecedent_unification[arg] = antecedent_args[i]
                                        elif antecedent_unification[arg] != antecedent_args[i]:
                                            break
                                else:
                                    unification.update(antecedent_unification)
                                    found = True

                    if not found:
                        antecedents_match = False
                        break

                if antecedents_match:
                    unifications.append(unification)
                    found_match = True
                    break  # Detener la búsqueda ya que se encontró una coincidencia con la regla

        if found_match:
            if unifications:
                for idx, unification in enumerate(unifications, start=1):
                    unification_str = ", ".join([f"'{key} = {value}'" for key, value in unification.items()])
                    print(f"Satisfacible, cuando {unification_str}. ¿Qué desea hacer?")
            else:
                print("No es satisfacible")


        else:
            print("No es satisfacible")

    else:
        print("Error: La expresión no está bien formada para una consulta")
