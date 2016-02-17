# Program:          Creating an Order
# Programmer:       wrekone
# Date:             2016.01.18
# Purpose:          The purpose of this program is to calculate the total cost of my grocery order.


# Input
# Declare Variables
print("Welcome to Kwik-E-Mart™ self-checkout. Don't forget to grab a Squishee™.")
item1_name = input("Item name? ")
item1_qty = int(input("Quantity? "))
item1_price = float(input("Price? $"))
item2_name = input("Item name? ")
item2_qty = int(input("Quantity? "))
item2_price = float(input("Price? $"))
item3_name = input("Item name? ")
item3_qty = int(input("Quantity? "))
item3_price = float(input("Price? $"))
my_name = input("Enter your name to claim your Super-Kwik-E Points™: ")

# Process
item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
item3_total = item3_qty * item3_price
order_total = item1_total + item2_total + item3_total


# Output
print()
print()
print("Order for", my_name)
print("Item", "Name   ", "Price", "Qty", "Total")
print()
print("1. {} {} {} {}".format(item1_name, item1_price, item1_qty, item1_total))
print()
print("2. {} {} {} {}".format(item2_name, item2_price, item2_qty, item2_total))
print()
print("3. {} {} {} {}".format(item3_name, item3_price, item3_qty, item3_total))
print()
print("Order Total:", "$" + str(order_total))
print()
print("You have earned", int(order_total / 5), "Super-Kwik-E Points™ today.")
print("Thank you. Come again.")

