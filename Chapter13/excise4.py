def addUpChange(quarters, dimes, nickels, pennies):
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return total

quarters = int(raw_input("quartes:"))
dimes = int(raw_input("dimes:"))
nickels = int(raw_input("nickels:"))
pennies = int(raw_input("pennies:"))

total = addUpChange(quarters, dimes, nickels, pennies)
print "You have a total of:", total
