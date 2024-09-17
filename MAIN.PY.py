import item

tax = 0.06
for price in cart:
    subtotal +=  item.price
grand_total = sub_total * tax
order_summary = "Total: ${:.2f}"
shop_again = True
while shop_again:


    while True:

        payment_type = input("How would you like to pay? (Cash/Credit/Check) ")

        if payment_type == "Cash":
            cash = input("Enter the amount of cash: ")
            break
        elif payment_type == "credit":

            card_num = input("Enter your credit card number: ")
            exp_date = input("Enter the expiration date: ")
            Cvv_num = input("Enter the CVV number: ")
            break
        elif payment_type == "check":
            check_num = input("Enter your check number: ")
            break
    print("Here is your receipt: ")
    print(f"{item_list}\nSubtotal: {sub_total}\n Grand Total: \n Payment option: {payment_type}")

shop_again = input("Would you like to shop again?(yes/no) ")
if shop_again == "no":
        break