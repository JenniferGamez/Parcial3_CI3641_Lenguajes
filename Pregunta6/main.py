# Jennifer Gamez
# 1610396

# Intérprete para un subconjunto del lenguaje Prolog:


from expression import *
from func_def_ask import*


# Menjador de interprete. Menu que ofrece el manejador
def main():
    print("Manejador intérprete para un subconjunto del lenguaje Prolog")
    print("Ingrese una acción (DEF <expresion> [<expresion>], ASK <expresion>, SALIR)")

    salir = False

    knowledge_base = KnowledgeBase()  # Para almacenar los hechos y reglas

    while not salir:
        accion = input(">")
        user_input = accion.strip()
        parts = user_input.split(' ', maxsplit=1)
        action = parts[0].upper()
        
        if action == 'DEF':
            if len(parts) > 1:
                expressions = re.findall(r'(\w+\([^)]+\))', parts[1])
                parsed_expressions = [exp.strip() for exp in expressions]
                process_def(parsed_expressions, knowledge_base)
                print()
            else:
                print("Error: La acción 'DEF' necesita al menos una expresión")
        
        elif action == 'ASK':
            if len(parts) > 1:
                process_ask(parts[1], knowledge_base)
            else:
                print("Error: La acción 'ASK' necesita una expresión")
        
        elif action == 'SALIR':
            print("Saliendo del simulador...")
            salir = True
            
        else:
            print("Acción no reconocida")


if __name__ == "__main__":
    main()
