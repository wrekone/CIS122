# A Video Game

# The Chess Champion

# A chess champion makes a bet. 
# He says "I'll place a penny on square one." 
# "Pay me $5 or double the amount on each square and pay me the total"
# Which bet would you place?

spaces = 1
dollars = .01
total_dollars = 0.0

while spaces < 65:
    print("For square {} earn ${}".format(spaces, dollars))
    total_dollars += dollars
    dollars *= 2
    spaces += 1

print("The champion earns ${}".format(total_dollars))
