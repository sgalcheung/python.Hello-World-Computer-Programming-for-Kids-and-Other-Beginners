import time

print "Countdown timer:",
start = int(raw_input("How many second?"))

for i in range (start, 0 ,-1):
    print i,
    for j in range (0, i):
        print " *",
    print
    time.sleep(1)
print "BLAST OFF!"
