print "Which multipllication table would you like?"
num = int(raw_input())
print "How high do you want to go?"
high = int(raw_input())
print "Here's your table:"
for i in range(1,high+1):
    print num,"x",i,"=",i*num
