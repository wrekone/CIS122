# Program:      Lesson 2 Calorie Counter
# Programmer:   wrekone
# Date:         2016.01.09
# Purpose:      The purpose of this program is to count the number of calories in a food item


# banner
print("Welcome to my calorie counter program")

# capture input
item_name = input("Please enter the item> ")
g_carbs = int(input("Enter grams of carbs> "))
g_fats = int(input("Enter grams of fats> "))
g_prot = int(input("Enter grams of proteins> "))

# do the math

cals = (g_carbs * 4) + (g_fats * 9) + (g_prot * 4)

# output

print("total calories for {} are {}".format(item_name, cals))
