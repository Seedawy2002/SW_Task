# string_expression.py
from .bases.base_expression import BaseExpression

class StringExpression(BaseExpression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value  # Return the literal string value
    
