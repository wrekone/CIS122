# Program:      Lesson 8 Calorie Counter
# Programmer:   Ben Abbott
# Date          2016.02.27
# Purpose:      The purpose of this program is to count the calories in a meal

# banner
print("Welcome to my calorie counter program")

# define variables
item_cnt = int(0)
tot_cals = int(0)
item_list = []
cals_list = []


# define functions

def input_name():
    valid_data = False

    while not valid_data:

        item_name = input("please enter the items> ")

        if len(item_name) > 14:
            print("not a valid food name")
        elif len(item_name) == 0:
            print("you need to enter a name")
        else:
            valid_data = True

    return item_name
    

def add_item(name, cals):
    item_list.append(name)
    cals_list.append(cals)


def del_item():
    if len(item_list) == 0:
        print("you have no menu items to delete")
    else:
        print("\nDelete an Item")
        disp_meal()

        valid_data = False
        while not valid_data:
            try:
                choice = int(input("Please enter the item number you would like to delete>"))
                if (choice-1) in range(len(item_list)):  # used instead of 1 <= choice <= range(len(item_list))

                    choice -= 1

                    print("Item {}. {} with {} calories will be deleted".format(choice + 1, item_list[choice], cals_list[choice]))

                    del item_list[choice]
                    del cals_list[choice]
                    valid_data = True

            except Exception as detail:
                print("error: ", detail)
                print("please try again")
                

def input_grams(element):
    valid_data = False

    while not valid_data:
        try:
            grams = int(input("enter grams of {}> ".format(element)))
            valid_data = True
        except Exception as detail:
            print("{} error: ".format(element), detail)

    return grams

    
def disp_menu():	
    choice_list = ["a", "d", "m", "q"]

    while True:
        print("What would you like to do?")
        print("a = add an item")
        print("d = delete an item")
        print("m = display the meal so far")
        print("q = quit")
        choice = input("make a selection>")

        if choice in choice_list:
            return choice
        else:
            print("I do not understand that entry. Try again.")



def add_process(tot_cals, item_cnt):
    item_name = input_name()
    g_carbs = input_grams("carbs")
    g_fats = input_grams("fats")
    g_prot = input_grams("protein")

  
    cals = calc_cals("c", g_carbs) + calc_cals("f", g_fats) + calc_cals("p", g_prot)


    print("total calories for {} are {}".format(item_name, cals))


    incl = input("would you like to include {}? (y/n)>".format(item_name))

    if incl.lower() == "y":
        add_item(item_name, cals)
        # accumulate totals
        tot_cals += cals
        item_cnt += 1
        print("item {} entered.".format(item_name))
        return tot_cals, item_cnt
    else:
        print("item {} not entered.".format(item_name))
        return tot_cals, item_cnt
    

def calc_cals(g_type, grams):
    if g_type == "f":
        return grams * 9
    else:
        return grams * 4
 

def disp_meal():
    print("\nMeal Calorie Counter")
    print("Num\tItem\t\tCals")
    print("---\t----\t\t----")
    meal_cals = 0

    for c in range(len(item_list)):
        meal_cals += cals_list[c]
        print("{}.\t{}\t\t{}".format(c+1, item_list[c], cals_list[c]))

    print("\nYour meal has {} items for a total of {} calories\n".format(len(item_list), meal_cals))
       
    
while True:
	
    choice = disp_menu()

    if choice == "a":
        tot_cals, item_cnt = add_process(tot_cals, item_cnt)
    elif choice == "d":
        del_item()
    elif choice == "q":
        break

    disp_meal()
    

disp_meal()

print("Thank you for using our program")
