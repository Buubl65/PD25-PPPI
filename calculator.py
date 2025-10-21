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
    """Ділить a на b (якщо b ≠ 0)"""
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")
    return a / b
