print "Which multiplication table would you like?"
num = int(raw_input())
print "Here's your table:"
for i in range(1,11):
    print num,"x",i,"=",num*i
