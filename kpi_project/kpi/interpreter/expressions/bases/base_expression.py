# base_expression.py
from abc import ABC, abstractmethod

class BaseExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass
