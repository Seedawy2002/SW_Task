# interpreter/expressions/operations/exponent_operation.py
from ..bases.base_operation import BaseOperation

class ExponentOperation(BaseOperation):
    def interpret(self, context):
        # Interpret the left and right sides and apply exponentiation
        return self.left.interpret(context) ** self.right.interpret(context)
