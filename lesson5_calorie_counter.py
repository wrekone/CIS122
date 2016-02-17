# Program:      Lesson 2 Calorie Counter
# Programmer:   wrekone
# Date:         2016.01.09
# Purpose:      The purpose of this program is to count the number of calories in a food item


# banner
print("Welcome to my calorie counter program")

# Declare Variables
meal_cals = 0
item_cnt = 0
cont = "y"

# Process
while cont.lower() == "y":
    # capture input
    item_name = input("Please enter the item> ")
    g_carbs = int(input("Enter grams of carbs> "))
    g_fats = int(input("Enter grams of fats> "))
    g_prot = int(input("Enter grams of proteins> "))

    # do the math
    
    item_cals = (g_carbs * 4) + (g_fats * 9) + (g_prot * 4)

    # accumulate meal totals

    item_cnt += 1
    meal_cals += item_cals

    # Output

    print("Your item {} has {}".format(item_name, item_cals))

    # prompt to see if the user wants to incluse this item

    print()
    incl = input("Would you like to include {}? (y.n)> ".format(item_name))

    if incl.lower() == "y":
        meal_cals += item_cals
        item_cnt += 1
        print("item {} entered. Total calories are now {}".format(item_name, meal_cals))
    else:
        print("item {} not entered. Total calories remain at {}".format(item_name, meal_cals))

    cont = input("Would you like to add another? y/n ")

# Output
print()
print("Your meal has {} items for a total of {} calories".format(item_cnt, meal_cals))
