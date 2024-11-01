# number_expression.py
from .bases.base_expression import BaseExpression

class NumberExpression(BaseExpression):
    def __init__(self, value):
        self.value = float(value)

    def interpret(self, context):
        return self.value