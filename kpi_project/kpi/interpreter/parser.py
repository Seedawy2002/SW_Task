# parser.py

from .expressions.function_expression import FunctionExpression
from .expressions.variable_expression import VariableExpression
from .expressions.number_expression import NumberExpression
from .expressions.string_expression import StringExpression
from .factory import ExpressionFactory

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current_token(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def next_token(self):
        self.index += 1
        return self.current_token()

    def peek_next_token(self):
        """Peek at the next token without consuming it."""
        return self.tokens[self.index + 1] if (self.index + 1) < len(self.tokens) else None

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        left = self.parse_term()
        while self.current_token() in ('+', '-'):
            operator = self.current_token()
            self.next_token()
            right = self.parse_term()
            left = ExpressionFactory.create_operation(operator, left, right)
        return left

    def parse_term(self):
        left = self.parse_exponent()
        while self.current_token() in ('*', '/'):
            operator = self.current_token()
            self.next_token()
            right = self.parse_exponent()
            left = ExpressionFactory.create_operation(operator, left, right)
        return left

    def parse_exponent(self):
        left = self.parse_factor()
        while self.current_token() == '^':
            operator = self.current_token()
            self.next_token()
            right = self.parse_factor()
            left = ExpressionFactory.create_operation(operator, left, right)
        return left

    def parse_factor(self):
        token = self.current_token()
        
        # Check for numbers
        if token.isdigit():
            self.next_token()
            return NumberExpression(float(token))
        
        # Check for strings (enclosed in double quotes)
        elif token.startswith('"') and token.endswith('"'):
            self.next_token()
            return StringExpression(token.strip('"'))
        
        # Check for variables and functions
        elif token.isalpha():
            next_token = self.peek_next_token()
            if next_token == '(':
                return self.parse_function_call(token)
            else:
                self.next_token()
                return VariableExpression(token)

        # Handle parentheses for precedence
        elif token == '(':
            self.next_token()  # Skip '('
            expression = self.parse_expression()
            self.next_token()  # Skip ')'
            return expression

    def parse_function_call(self, function_name):
        """Parse a function call like regex("doghouse", "^dog")"""
        self.next_token()  # Skip the function name
        self.next_token()  # Skip '('

        arguments = []
        while self.current_token() != ')':
            arguments.append(self.parse_expression())
            if self.current_token() == ',':
                self.next_token()  # Skip ','

        self.next_token()  # Skip ')'
        return FunctionExpression(function_name, arguments)
