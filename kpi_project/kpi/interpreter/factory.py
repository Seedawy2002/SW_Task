# factory.py
from .expressions.number_expression import NumberExpression
from .expressions.string_expression import StringExpression
from .expressions.variable_expression import VariableExpression
from .expressions.function_expression import FunctionExpression
from .expressions.operations.add_operation import AddOperation
from .expressions.operations.subtract_operation import SubtractOperation
from .expressions.operations.multiply_operation import MultiplyOperation
from .expressions.operations.divide_operation import DivideOperation
from .expressions.operations.exponent_operation import ExponentOperation

# interpreter/factory.py

from .expressions.operations.add_operation import AddOperation
from .expressions.operations.subtract_operation import SubtractOperation
from .expressions.operations.multiply_operation import MultiplyOperation
from .expressions.operations.divide_operation import DivideOperation
from .expressions.operations.exponent_operation import ExponentOperation

class ExpressionFactory:
    @staticmethod
    def create_operation(operator, left, right):
        if operator == '+':
            return AddOperation(left, right)
        elif operator == '-':
            return SubtractOperation(left, right)
        elif operator == '*':
            return MultiplyOperation(left, right)
        elif operator == '/':
            return DivideOperation(left, right)
        elif operator == '^':  # Register the exponentiation operator
            return ExponentOperation(left, right)
        else:
            raise ValueError(f"Unknown operator: {operator}")

from .functions.regex_function import regex

functions = {
    # other functions
    'regex': regex,
}
