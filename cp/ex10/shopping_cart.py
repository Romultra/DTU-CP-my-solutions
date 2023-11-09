"""This file contains the project's code and solution."""
class Item:
    """A class to represent an inventory item.""" 

    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __lt__(self, other):
        if self.quantity * self.price < other.quantity * other.price:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.quantity * self.price > other.quantity * other.price:
            return True
        else:
            return False
        
    def __eq__(self, other):
        if self.quantity * self.price == other.quantity * other.price:
            return True
        else:
            return False

class Inventory(list):
    """A class to represent an inventory of items."""
    
    def add_item(self, item : Item):
        self.append(item)

    def calculate_total_value(self):
        total_value = 0
        for item in self:
            total_value += item.quantity * item.price
        
        return total_value
    
    def __lt__(self, other):
        if self.calculate_total_value() < other.calculate_total_value():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.calculate_total_value() > other.calculate_total_value():
            return True
        else:
            return False
        
    def __eq__(self, other):
        if self.calculate_total_value() == other.calculate_total_value():
            return True
        else:
            return False
