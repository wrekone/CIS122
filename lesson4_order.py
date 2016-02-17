# Program       Lesson 4 Order
# Programmer    Ben Abbott
# Date          2016.01.28
# Purpose       The purpose of this program is to calculate the total cost of a grocery order

# Define Variables
cont = ""
item_cnt = 0
item_name = ""
item_qty = 0
item_price = 0.0
order_total = 0.0
item_total = 0.0
cust = ""

# Banner
print("Welcome to Smallville Grocer.")
      
# Input
cont = input("Would you like to place an order? (y/n) ")
cust = input("Enter your name to collect your frequent shopper points: ")
print()
print("Order for", cust)
print()

# Process
while cont.lower() == "y":
    item_cnt += 1
    item_name = input("Item name: ")
    
    item_qty = int(input("Quantity: "))
    item_price = float(input("Price: $"))
    print()
    item_total = item_price * item_qty
    order_total += item_total
    print("Item  ", "Name   ", "Qty ", "Price ", "Total")
    print("--------------------------------")
    print("{}. {} {} ${} ${}".format(item_cnt, item_name, item_qty, item_price, item_total))
    print("Subtotal: $" + str(order_total))
    print()
    cont = input("Would you like to add another” (y/n) ")
    print()

# Output
print("You ordered {} items for a total price of ${}".format(item_cnt, order_total))
print("Thank you for your order", cust)
