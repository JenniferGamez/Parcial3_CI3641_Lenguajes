import unittest
from func_def_ask import*
from expression import *

class TestExpression(unittest.TestCase):
    def test_atom_expression(self):
        # Prueba para expresiones tipo átomo
        atom_exp = Expression("hola")
        self.assertEqual(atom_exp.type, "Atomo")

    def test_variable_expression(self):
        # Prueba para expresiones tipo variable
        var_exp = Expression("Variable")
        self.assertEqual(var_exp.type, "Variable")

    def test_structure_expression(self):
        # Prueba para expresiones tipo estructura
        struct_exp = Expression("f(x, y)")
        self.assertEqual(struct_exp.type, "Estructura")

class TestProcess(unittest.TestCase):
    def setUp(self):
        # Crea una base de conocimientos vacía para cada prueba
        self.knowledge_base = KnowledgeBase()

    def test_define_fact(self):
        # Prueba para definir un hecho
        expressions = ["padre(juan, jose)"]
        process_def(expressions, self.knowledge_base)
        self.assertEqual(len(self.knowledge_base.facts), 1)
        self.assertEqual(self.knowledge_base.facts[0].predicate_name, "padre")
        self.assertEqual(self.knowledge_base.facts[0].args, ['juan', 'jose'])

    def test_define_rule(self):
        # Prueba para definir una regla
        expressions = ["ancestro(X, Y)", "padre(X, Y)"]
        process_def(expressions, self.knowledge_base)
        self.assertEqual(len(self.knowledge_base.rules), 1)
        self.assertEqual(self.knowledge_base.rules[0].predicate_name, "ancestro")
        self.assertEqual(self.knowledge_base.rules[0].args, (['X', 'Y']))
        self.assertEqual(self.knowledge_base.rules[0].antecedents, (["padre(X, Y)"]))

    def test_invalid_expression(self):
        # Prueba para una expresión mal formada
        expressions = ["incorrect_expression"]
        process_def(expressions, self.knowledge_base)
        self.assertEqual(len(self.knowledge_base.facts), 0)
        self.assertEqual(len(self.knowledge_base.rules), 0)

    class TestProcessAsk(unittest.TestCase):
        def test_process_ask(self):
            # Simular la base de conocimientos
            knowledge_base = KnowledgeBase()

            # Agregar hechos a la base de conocimientos
            fact1 = Fact("padre", ["jose", "pablo"])
            fact2 = Fact("padre", ["pablo", "gaby"])
            knowledge_base.add_fact(fact1)
            knowledge_base.add_fact(fact2)

            # Agregar reglas a la base de conocimientos
            rule1 = Rule("ancestro", ["X", "Y"], "padre(X, Y)")
            rule2 = Rule("ancestro", ["X", "Y"], "padre(X, Z)", "ancestro(Z, Y)")
            knowledge_base.add_rule(rule1)
            knowledge_base.add_rule(rule2)

            # Realizar pruebas con expresiones específicas
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                process_ask("ancestro(X, gaby)", knowledge_base)
                self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    "Satisfacible, cuando 'X = jose'. ¿Qué desea hacer?"
                )

                process_ask("ancestro(gaby, X)", knowledge_base)
                self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    "No es satisfacible"
                )

if __name__ == '__main__':
    unittest.main()
