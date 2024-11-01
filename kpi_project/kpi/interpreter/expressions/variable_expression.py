from .bases.base_expression import BaseExpression

# VariableExpression.py

class VariableExpression(BaseExpression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        if self.name in context:
            return context[self.name]  # Look up in the context if it exists
        else:
            # Handle missing variables or raise an informative error
            raise KeyError(f"'{self.name}' not found in context")

