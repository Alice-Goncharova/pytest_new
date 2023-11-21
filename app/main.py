from typing import Union
import math
from app.error import InvalidInputException

numeric = Union[int, float]


class Calculator:

    @staticmethod
    def sum(*args):
        for arg in args:
            if not isinstance(arg, numeric):
                raise TypeError
        return sum(args)

    @staticmethod
    def subtract(a: numeric, b: numeric) -> numeric:
        return a - b

    @staticmethod
    def multiply(a: numeric, b: numeric) -> numeric:
        return a * b

    @staticmethod
    def divide(a: numeric, b: numeric) -> numeric:
        return a / b

    def log(self, a: numeric, base: numeric) -> numeric:
        if not isinstance(a, (int, float)) or not isinstance(base, (int, float)):
            raise TypeError("Both 'a' and 'base' must be a number")
        if base == 0:
            raise TypeError("'base' must not be zero")
        if a <= 0 or base <= 0:
            raise InvalidInputException("Both 'a' and 'base' must be positive")
        # TODO: cover this method with unit-tests
        if a > 0 and a != 1 and base > 0:
            return math.log(a, base)
        else:
            raise InvalidInputException(self.log, a, base)


calc = Calculator()

