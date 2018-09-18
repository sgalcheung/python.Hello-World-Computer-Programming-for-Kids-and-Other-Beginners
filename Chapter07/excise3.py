tankSize = int(raw_input("How big is your tank(liters)?"))
full = int(raw_input("How full is yoour tank (eg. 50 for half full)?"))
mileage = int(raw_input("What is your gas mileage(km per liter)?"))
range = (tankSize - 5) * (full / 100.0) * mileage
print "You can go another",range,"km"
print "The next gas station is 200km away."
if range < 200:
    print "Get gas now!"
else:
    print "You can wait for the next station."
