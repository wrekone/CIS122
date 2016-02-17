# Program       Lesson 7 Order
# Programmer    Ben Abbott
# Date          2016.02.16
# Purpose       The purpose of this program is to take an order for cookies.


# Import Class/Format Currency
import locale
locale.setlocale(locale.LC_ALL, '')
from datetime import datetime

# Define Variables
boxes = 0
qty = 0
cost = 3.50
items = 0
yorn = ["y", "n"]

# Define Functions
def disp_menu():
	print("Please choose a flavor:")
	print("1. Savannahs")
	print("2. Thin Mints")
	print("3. Tagalongs")

def calc_item():
	return cost * qty
	
def print_order():
	True

now = datetime.now()

# Banner
print("Welcome to The Cookie Portal")
print("%s/%s/%s" % (now.month, now.day, now.year))
      
# Input
valid_data = False

while not valid_data:
	name = input("Please enter your name: ")
	if len(name) > 20:
		print("Not a valid name")
		valid_data = False
	elif len(name) == 0:
		print("You need to enter a name")
		valid_data = False
	else:
		print("Hello", name)
		valid_data = True

cont = input("Would you like to place an order? (y/n) ")

# Process
while cont.lower() not in yorn:
    cont = input("Would you like to place an order? (y/n) ")

while cont.lower() == "y":
	
	valid_data = False
	
	while not valid_data:
		disp_menu()
		try:
			flavor = int(input("> "))
			if flavor in range (1, 4):
				items += 1
				valid_data = True
			else:
				valid_data = False
		except Exception as detail:
			print("Error", detail)

	valid_data = False
	
	while not valid_data:
		try:
			boxes = int(input("How many boxes? (1-10) "))
			if boxes not in range (1, 11):
				print("Please choose a number between 1 and 10")
				valid_data = False
			else:
				qty += boxes
				valid_data = True
		except Exception as detail:
			print("Error", detail)
			print("Please enter a number")
			
	valid_data = False
	
	while not valid_data: #why can't I get out of this loop?
		cont = input("Would you like to order another? (y/n) ")
		if cont.lower() not in yorn:
			valid_data = False
		else:
			valid_data = True
		


# Output
if cont.lower() == "n":      
	print()
	print("Order for", name)
	print("%s:%s:%s   %s/%s/%s" % (now.hour, now.minute, now.second, now.month, now.day, now.year))
	print("-------------------")
	print("Total Items = {}".format(items))
	print("Total Boxes = {}".format(qty))
	print("Total Cost = {}".format(locale.currency(calc_item())))
	print()

	print("Thank you for your order.")

