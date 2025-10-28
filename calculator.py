def validate_divisor(b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")

class Calculator:
    """Простий клас калькулятора"""

    def add(self, a, b):
        """Додає два числа"""
        return a + b

    def subtract(self, a, b):
        """Віднімає b від a"""
        return a - b

    def multiply(self, a, b):
        """Множить два числа"""
        return a * b

    def divide(self, a, b):
        """Ділить a на b з перевіркою"""
        validate_divisor(b)
        return a / b
    
    def discount(self, price, percent):
        """Розраховує ціну зі знижкою"""
        if percent < 0 or percent > 100:
            raise ValueError("Знижка має бути від 0 до 100%")
        return price * (1 - percent / 100)

    def add_vat(self, price, vat_percent):
        """Додає ПДВ до ціни"""
        return price * (1 + vat_percent / 100)

    def remove_vat(self, price, vat_percent):
        """Віднімає ПДВ з ціни"""
        return price / (1 + vat_percent / 100)
