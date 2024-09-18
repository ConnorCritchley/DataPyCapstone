# Connor Critchley
# Python Capstone, 9/11/24
from openpyxl.styles.builtins import total

#from main import quantity


class Item:  # Baseline parent Item class

    def __init__(self, name, price, quantity):  # Takes a name and price
        self.category = "General"
        self.name = name  # assigns passed in name and price to item instance
        self.price = price
        self.quantity = quantity
        self.total = self.quantity * self.price



    def __str__(self):
        return f"{self.quantity} {self.name}(s) that costs ${self.total:.2f}"


class Drink(Item):  # Item subclass for drinks
    def __init__(self, name, price, size, quantity):  # Takes in name and price, and size
        self.size = size  # assigns drink-specific size variable
        Item.__init__(self, name, price, quantity)  # calls parent constructor for other details
        self.category = "Drink"
        self.upcharge = 0.30 if size == 'L' else 0
        self.price += self.upcharge
        self.total = self.quantity * self.price

    def __str__(self):
        if self.size == 'L':
            return f"{self.quantity} large {self.name}(s) (including $0.30 upcharge per item) that costs ${self.total:.2f}"
        else:
            return f"{self.quantity} regular {self.name}(s) that costs ${self.total:.2f}"


class Food(Item):  # Item subclass for Food
    def __init__(self, name, price, toasted, quantity):  # Takes in name and price, and if toasted
        self.toasted = toasted  # Assigns food-specific
        Item.__init__(self, name, price, quantity)
        self.category = 'Food'

    def __str__(self):
        return f"{self.quantity} {'toasted' if self.toasted else 'plain'} {self.name}(s) that costs ${self.total:.2f}"

if __name__ == '__main__':
    print("Not intended to be run on it's own.")
