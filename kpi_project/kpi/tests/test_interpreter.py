# test_interpreter.py
import unittest
from kpi.interpreter.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def test_addition(self):
        expression = "3 + 5"
        interpreter = Interpreter(expression)
        context = {}
        result = interpreter.interpret(context)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        expression = "10 - 4"
        interpreter = Interpreter(expression)
        context = {}
        result = interpreter.interpret(context)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        expression = "7 * 3"
        interpreter = Interpreter(expression)
        context = {}
        result = interpreter.interpret(context)
        self.assertEqual(result, 21)

    def test_division(self):
        expression = "20 / 4"
        interpreter = Interpreter(expression)
        context = {}
        result = interpreter.interpret(context)
        self.assertEqual(result, 5.0)

    def test_exponentiation(self):
        expression = "2 ^ 3"
        interpreter = Interpreter(expression)
        context = {}
        result = interpreter.interpret(context)
        self.assertEqual(result, 8)

    def test_parentheses(self):
        expression = "(2 + 3) * 4"
        interpreter = Interpreter(expression)
        context = {}
        result = interpreter.interpret(context)
        self.assertEqual(result, 20)

    def test_variable_substitution(self):
        expression = "value * 2 + 3"
        interpreter = Interpreter(expression)
        context = {"value": 4}
        result = interpreter.interpret(context)
        self.assertEqual(result, 11)

if __name__ == "__main__":
    unittest.main()
