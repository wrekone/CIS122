# Program:      Lesson 2 Calorie Counter
# Programmer:   wrekone
# Date:         2016.01.09
# Purpose:      The purpose of this program is to count the number of calories in a food item


# create variables
g_carbs = 5
g_fats = int(5)
g_prot = 4

item_name = "banana"

# do the math

cals = (g_carbs * 4) + (g_fats * 9) + (g_prot * 4)

# output

print("total calories for {} are {}".format(item_name, cals))
