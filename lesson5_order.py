# Program       Lesson 5 Order
# Programmer    wrekone
# Date          2016.02.02
# Purpose       The purpose of this program is to take an order for cookies.


# Import Class/Format Currency
import locale
locale.setlocale(locale.LC_ALL, '')

# Define Variables
boxes = 0
cost = 3.50
flavor = 0
qty = 0
name = ""
flavor_list = ["1", "2", "3"]
qty_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
item_list = []

# Banner
print("Welcome to The Cookie Portal")
      
# Input
cont = input("Would you like to place an order? (y/n) ")

# Process
while cont.lower() not in ("y", "n"):
    cont = input("Would you like to place an order? (y/n) ")
while cont.lower() == "n":
    print("Thank you. Please shop with us again.")
    break
while cont.lower() == "y":
    name = input("Enter your name to collect your frequent shopper points: ")
    while cont.lower() == "y":
        print("Please choose a flavor:")
        print("1. Savannahs")
        print("2. Thin Mints")
        print("3. Tagalongs")
        flavor = input("> ")
        while flavor not in flavor_list:
            print()
            print("Please enter a value between 1 and 3")
            print("1. Savannahs")
            print("2. Thin Mints")
            print("3. Tagalongs")
            flavor = input("> ")
        if flavor == ("1"):
            qty = input("How many would you like? (1-10)> ")
            while qty not in (qty_list):
                print()
                print("Please enter a value between 1 and 10")
                qty = input("How many would you like? (1-10)> ")
            print()
            print(qty, "Savannahs added to your cart")
            print()
            boxes += int(qty)
            if "Savannahs" not in item_list:
                item_list.append("Savannahs")
        elif flavor == ("2"):
            qty = input("How many would you like? (1-10)> ")
            while qty not in (qty_list):
                print()
                print("Please enter a value between 1 and 10")
                qty = input("How many would you like? (1-10)> ")
            print()
            print(qty, "Thin Mints added to your cart")
            print()
            boxes += int(qty)
            if "Thin Mints" not in item_list:
                item_list.append("Thin Mints")
        elif flavor == ("3"):
            qty = input("How many would you like? (1-10)> ")
            while qty not in (qty_list):
                print()
                print("Please enter a value between 1 and 10")
                qty = input("How many would you like? (1-10)> ")
            print() 
            print(qty, "Tagalongs added to your cart")
            print()
            boxes += int(qty)
            if "Tagalongs" not in item_list:
                item_list.append("Tagalongs")
        cont = input("Would you like to order another? (y/n) ")
        while cont.lower() not in ("y", "n"):
            cont = input("Would you like to order another? (y/n) ")
    cost *= boxes
    
# Output
    if cont.lower() == "n":      
        print()
        print("Order for", name)
        print("-------------------")
        print("Total Items = {}".format(len(item_list)))
        print("Total Boxes = {}".format(boxes))
        print("Total Cost = {}".format(locale.currency(cost)))
        print()
        print("Thank you for your order.")
