import random
import time

print "Work for 30 seconds, print a random number every three seconds."
for i in range(10):
    number = random.random()
    print number
    time.sleep(3)
