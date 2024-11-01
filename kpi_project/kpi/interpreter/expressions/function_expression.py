# function_expression.py
import re
from .bases.base_expression import BaseExpression

class FunctionExpression(BaseExpression):
    def __init__(self, function_name, args):
        self.function_name = function_name
        self.args = args  # Make sure args is initialized

    def interpret(self, context):
        # Evaluate each argument in the current context
        evaluated_args = [
            arg.interpret(context) if isinstance(arg, BaseExpression) else arg
            for arg in self.args
        ]
        
        # Retrieve and call the function from context, passing evaluated arguments
        function = context.get(self.function_name)
        if function:
            return function(*evaluated_args)  # Ensure correct number of args are passed
        else:
            raise ValueError(f"Function '{self.function_name}' not found in context.")

    def evaluate_regex(self, text, pattern):
        # Verify both arguments are strings
        if not isinstance(text, str) or not isinstance(pattern, str):
            raise TypeError("Arguments to regex must be strings")
        return bool(re.match(pattern, text))
