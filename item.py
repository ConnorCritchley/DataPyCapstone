# Connor Critchley
# Python Capstone, 9/11/24

class Item:  # Baseline parent Item class
    def __init__(self, name, price):  # Takes a name and price
        self.name = name  # assigns passed in name and price to item instance
        self.price = price


class Drink(Item):  # Item subclass for drinks
    def __init__(self, name, price, size):  # Takes in name and price, and size
        self.category = "Drink"
        self.size = size  # assigns drink-specific size variable
        Item.__init__(self, name, price)  # calls parent constructor for other details
        if size == 'L':  # If they ordered a large, increase price by .30
            self.price += 0.3


class Food(Item):  # Item subclass for Food
    def __init__(self, name, price, toasted):  # Takes in name and price, and if toasted
        self.toasted = toasted  # Assigns food-specific
        self.category = 'Food'
        Item.__init__(self, name, price)

if __name__ == '__main__':
    print("Not intended to be run on it's own.")
