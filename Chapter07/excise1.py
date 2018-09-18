cost =float(raw_input("Total purchase price:"))
if cost <= 10:
    discount = 0.1
    print '''The purchase amount is no more than ten yuan,giving you a 10% discount.'''
    print "The final price is",(1 - discount) * cost
else:
    discount = 0.2
    print "The purchase amount exceeds ten yuan, giving you a 20% discount."
    print "The final price is",(1 - discount) * cost
