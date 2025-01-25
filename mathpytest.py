#functions
#Updated on 01-25-25
class MathUtils:

    def add(a, b):
        return a + b

    # @staticmethod
    def subtract(a, b):
        return a - b

    # @staticmethod
    def multiply(a, b):
        return a * b

    # @staticmethod
    def divide(a, b):
        if b == 0:
            return -1.0
        return a / b
