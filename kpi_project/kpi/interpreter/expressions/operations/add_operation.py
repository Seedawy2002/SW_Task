# add_operation.py
from ..bases.base_operation import BaseOperation

class AddOperation(BaseOperation):
    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)
