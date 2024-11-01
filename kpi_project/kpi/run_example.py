# run_example.py
from kpi.interpreter.interpreter import Interpreter

if __name__ == "__main__":
    #expression = 'regex(value, "^dog")'
    #context = {"value":"doghouse"}4#expression = 'regex(value, "^dog")'

    expression = 'value * 5'
    context = {"value":1}

    interpreter = Interpreter(expression)
    result = interpreter.interpret(context)

    print(f"Result of regex expression: {result}")  # Expected: True
