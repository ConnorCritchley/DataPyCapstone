# Plan C
#from pandas.conftest import join_type

import item as I

# hardcoded menu dictionary
menu = {"Espresso": 2.49, "Cappuccino": 3.99, "Latte": 4.49, "Americano": 2.99,
        "Mocha": 4.99, "Cold Brew": 4.29, "Iced Coffee": 3.49, "Matcha Latte": 5.29,
        "Chai Tea Latte": 4.79, "Bagel": 2.79, "Croissant": 2.49, "Avocado Toast": 5.59,
        "Chicken Wrap": 6.59, "Club Sandwich": 6.79}
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
    menu_keys[len(menu)-1] = name
    print_menu()


def print_menu():
    print("{:<5} {:<15} {:<10}".format('Item', 'Name', 'Price'))
    index = 0
    for key, value in menu.items():
        index += 1
        print("{:<5} {:<15} ${:<10}".format(index, key, value))


# main loop
while running:
    print("\n------Welcome to StarCreek Coffee-------")

    # print out menu
    cart = []
    # primary interaction
    ordering = True
    while ordering:
        choice = ""
        valid = False
        while not valid:
            choice = input("Make a selection or add to the menu? Type 'select' to view menu or 'add' to add a new item: \n")
            if choice.upper() in "SELECT" or "ADD":
                match choice.upper():
                    case 'SELECT':
                        print_menu()
                        valid = True
                    case 'ADD':
                        add_item()
                    case _:
                        pass

        valid = False
        while not valid:
            choice = int(input("Make a selection(Enter item number):\n")) - 1
            if choice in range(len(menu)):
                valid = True

        # User chooses quantity of item
        valid_quantity = False
        quantity = 0
        while not valid_quantity:
            try:
                quantity = int(input("Enter a quantity for item: "))
                if quantity > 0:
                    valid_quantity = True
            except ValueError:
                print("Enter a valid quantity")

        # at this state, we can only have a valid number selection
        # Check if it's in the drink section
        if choice in range(9):
            # Choice is Drink
            size = ''
            valid = False
            while not valid:
                size = input("What's the drink's size? Regular ('R') or Large ('L')? Large is +$0.30\n").upper()
                if size == 'R' or 'L':
                    valid = True
            cart.append(I.Drink(menu_keys[choice], menu[menu_keys[choice]], size, quantity))
        # Check if in the food section
        elif choice in range(9, 14):
            toasted = True if input("Want it toasted? y/n\n").upper() == 'Y' else False
            cart.append(I.Food(menu_keys[choice], menu[menu_keys[choice]], toasted, quantity))
        # check for custom item added to menu, anything higher than our preset ones
        elif choice >= 14:
            cart.append(I.Item(menu_keys[choice], menu[menu_keys[choice]], quantity))
        # Check for exit of ordering loop
        if input('Checkout? y/n\n').upper() == 'Y':
            ordering = False
        for item in cart:
            print(item)

    # Now out of ordering loop, do payment processing/receipt stuff
    # DO HERE
    tax = 0.06
    subtotal = 0
    for item in cart:
        subtotal += item.price * item.quantity
    grand_total = (subtotal * tax) + subtotal
    print(f"Subtotal: ${subtotal:.2f}\nTax: ${subtotal * tax:.2f}\nGrand Total: ${grand_total:.2f}")
    payment_type = input("How would you like to pay? (Cash/Credit/Check)\n").upper()
    cash = 0
    change = 0
    if payment_type == "CASH":
        cash = float(input("Enter the amount of cash: "))
        if cash < grand_total:
            print("You need more cash")
    elif payment_type == "CREDIT":
        card_num = input("Enter your credit card number: ")
        exp_date = input("Enter the expiration date: ")
        Cvv_num = input("Enter the CVV number: ")
    elif payment_type == "CHECK":
        check_num = input("Enter your check number: ")
    print("------Here is your receipt------- ")
    for item in cart:
        print(item)
    print(f"Payment option: {payment_type}")
    if payment_type == 'CREDIT':
        print(f"Credit acct: **********{card_num[-5:-1]}")
    elif payment_type == 'CASH':
        change = grand_total - cash
        if change == 0:
            pass
        else:
            print(f"Change is ${abs(change):.2f}")

    # Check for exit of main run loop
    if input('\nOrder again? y/n\n').upper() == 'N':
        print("Thank you for shopping!")
        running = False

