from ..bases.base_operation import BaseOperation

class MultiplyOperation(BaseOperation):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) * self.right.interpret(context)