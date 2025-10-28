def validate_divisor(b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")

class Calculator:

    def add(a, b):
        """Додає два числа"""
        return a + b

    def subtract(a, b):
        """Віднімає b від a"""
        return a - b

    def multiply(a, b):
        """Множить два числа"""
        return a * b

    def divide(a, b):
        validate_divisor(b)
        return a / b
