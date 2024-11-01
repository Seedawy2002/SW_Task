# base_operation.py
from abc import ABC, abstractmethod
from .base_expression import BaseExpression

class BaseOperation(BaseExpression, ABC):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @abstractmethod
    def interpret(self, context):
        pass  # Each subclass implements its specific operation
