# Plan C

import item as I

# hardcoded menu dictionary
menu = {"Espresso": 2.50, "Cappuccino": 4.00, "Latte": 4.50, "Americano": 3.00,
        "Mocha": 5.00, "Cold Brew": 4.25, "Iced Coffee": 3.50, "Matcha Latte": 5.25,
        "Chai Tea Latte": 4.75, "Bagel": 2.75, "Croissant": 2.50, "Avocado Toast": 5.50,
        "Chicken Caesar Wrap": 6.50, "Club Sandwich": 6.75}
menu_keys = {0: "Espresso", 1: "Cappuccino", 2: "Latte", 3: "Americano",
             4: "Mocha", 5: "Cold Brew", 6: "Iced Coffee", 7: "Matcha Latte",
             8: "Chai Tea Latte", 9: "Bagel", 10: "Croissant", 11: "Avocado Toast",
             12: "Chicken Wrap", 13: "Club Sandwich"}
running = True  # main running bool


# function adds a new menu item to the menu based on user input
def add_item():
    # get main values
    name = input("What is your item called?\n")
    price = None
    valid = False
    while not valid:
        try:
            price = float(input("What is a fair price for the item?\n"))
            valid = True
        except ValueError:
            pass
    menu[name] = price
    menu_keys.update({len(menu)-1:name})
    print_menu()


def print_menu():
    print("{:<5} {:<15} {:<10}".format('Item', 'Name', 'Price'))
    index = 0
    for key, value in menu.items():
        index += 1
        print("{:<5} {:<15} ${:<10}".format(index, key, value))


# main loop
while running:
    # print out menu
    print_menu()

    # primary interaction
    ordering = True
    while ordering:
        choice = ""
        cart = []
        valid = False
        while not valid:
            choice = input("Make a selection or add to the menu? Type 'select' or 'add'\n")
            if choice.upper() in "SELECT" or "ADD":
                match choice.upper():
                    case 'SELECT':
                        valid = True
                    case 'ADD':
                        add_item()
                    case _:
                        pass

        valid = False
        while not valid:
            choice = int(input("Make a selection:\n")) - 1
            if choice in range(len(menu)):
                valid = True

        # at this state, we can only have a valid number selection
        # Check if it's in the drink section
        if choice in range(9):
            # Choice is Drink
            size = ''
            valid = False
            while not valid:
                size = input("What's the drink's size? Regular ('R') or Large ('L')?\n").upper()
                if size == 'R' or 'L':
                    valid = True
            cart.append(I.Drink(menu_keys[choice], menu[menu_keys[choice]], size))
        # Check if in the food section
        elif choice in range(10, 14):
            toasted = True if input("Want it toasted? y/n\n").upper() == 'Y' else False
            cart.append(I.Food(menu_keys[choice], menu[menu_keys[choice]], toasted))
        # check for custom item added to menu, anything higher than our preset ones
        elif choice >= 14:
            print("reached custom item")
            cart.append(I.Item(menu_keys[choice], menu[menu_keys[choice]]))
        # Check for exit of ordering loop
        if input('Checkout? y/n\n').upper() == 'Y':
            ordering = False

        print(cart[0])

    # Now out of ordering loop, do payment processing/receipt stuff
    # DO HERE


    # Check for exit of main run loop
    if input('Order again? y/n\n').upper() == 'N':
        running = False
