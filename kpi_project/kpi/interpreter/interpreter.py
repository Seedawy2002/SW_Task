import re
from .parser import Parser
from .tokenizer import tokenize
from .functions.regex_function import regex  # Import the regex function

class Interpreter:
    def __init__(self, expression):
        self.tokens = tokenize(expression)
        self.parser = Parser(self.tokens)

    def interpret(self, context):
        # Register functions in the context
        extended_context = context.copy()
        extended_context["regex"] = regex  # Make regex available in the interpreter
        syntax_tree = self.parser.parse()
        return syntax_tree.interpret(extended_context)
