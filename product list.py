# Parent class for Product
class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


# Subclass for Beverages
class Beverage(Product):
    def __init__(self, name, price):
        super().__init__(name, "Beverage", price)


# Subclass for Food
class Food(Product):
    def __init__(self, name, price):
        super().__init__(name, "Food", price)


# Function to display the menu
def display_menu(products):
    print("\n--- Coffee Shop Menu ---")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product.name} ({product.category}) - ${product.price:.2f}")
    print()


# Function to handle item selection and quantity
def select_item(products):
    while True:
        try:
            choice = int(input("Enter the item number to order (or 0 to checkout): "))
            if 0 <= choice <= len(products):
                if choice == 0:
                    return None
                quantity = int(input(f"Enter quantity for {products[choice - 1].name}: "))
                return (products[choice - 1], quantity)
            else:
                print("Invalid choice, please select a valid item number.")
        except ValueError:
            print("Invalid input, please enter numbers only.")

# Main program logic
def main():
    # List of coffee shop products
    products = [
        Beverage("Espresso", 2.50),
        Beverage("Cappuccino", 4.00),
        Beverage("Latte", 4.50),
        Beverage("Americano", 3.00),
        Beverage("Mocha", 5.00),
        Beverage("Cold Brew", 4.25),
        Beverage("Iced Coffee", 3.50),
        Beverage("Matcha Latte", 5.25),
        Beverage("Chai Tea Latte", 4.75),
        Food("Bagel with Cream Cheese", 3.00),
        Food("Blueberry Muffin", 2.75),
        Food("Croissant", 2.50),
        Food("Avocado Toast", 5.50),
        Food("Chicken Caesar Wrap", 6.50),
        Food("Chocolate Chip Cookie", 1.75),
    ]


# Run the program
if __name__ == "__main__":
    main()