# Program       Name and birthdate
# Programmer    wrekone
# Date          2016.01.15
# Purpose       The purpose of this program is to say nice things about the user

# Input
name1 = input("What is your first name? ")
name2 = input("What is your last name? ")
month = input("What month were you born in? ")
day = input("What day of the month were you born? ")
year = int(input("What year were you born? "))
gender = input("Are you a guy or a gal? ")

# Process
full_name = (name1 + " " + name2)
dob = month + " " + day + ", " + str(year)
       
# Output
print()
print("So", name1, "what you're saying is...")
print("You were born on", dob + "?")
print(name1, "you are a lucky", gender + "!")
print(dob, "is a very auspicious day.")
print()

# Input
hair = input("What color is your hair? ")
eyes = input("What color are your eyes? ")

# Process
tone = hair + " " + "hair and" + " " + eyes + " " + "eyes"

# Output
print()
print("Wow,", tone + "!")
print(full_name, "you sound like a lovely", gender + "!")
print("I think I'm in love.")
print("Computer love...")
