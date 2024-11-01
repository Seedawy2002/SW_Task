# divide_operation.py
from ..bases.base_operation import BaseOperation

class DivideOperation(BaseOperation):
    def interpret(self, context):
        right_value = self.right.interpret(context)
        if right_value == 0:
            raise ValueError("Division by zero")
        return self.left.interpret(context) / right_value
