# Connor Critchley
# Python Capstone, 9/11/24

class Item:  # Baseline parent Item class
    def __init__(self, name, price):  # Takes a name and price
        self.category = "General"
        self.name = name  # assigns passed in name and price to item instance
        self.price = price

    def __str__(self):
        return f"A {self.name} that costs ${self.price:.2f}"


class Drink(Item):  # Item subclass for drinks
    def __init__(self, name, price, size):  # Takes in name and price, and size
        self.size = size  # assigns drink-specific size variable
        Item.__init__(self, name, price)  # calls parent constructor for other details
        self.category = "Drink"
        if size == 'L':  # If they ordered a large, increase price by .30
            self.price += 0.3

    def __str__(self):
        return f"A {'large' if self.size == 'L' else 'regular'} {self.name} that costs ${self.price:.2f}"


class Food(Item):  # Item subclass for Food
    def __init__(self, name, price, toasted):  # Takes in name and price, and if toasted
        self.toasted = toasted  # Assigns food-specific
        Item.__init__(self, name, price)
        self.category = 'Food'

    def __str__(self):
        return f"A {'toasted' if self.toasted else 'plain'} {self.name} that costs ${self.price:.2f}"

if __name__ == '__main__':
    print("Not intended to be run on it's own.")
