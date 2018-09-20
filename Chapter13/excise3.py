def calculateTax(price, tax_tate):
    total = price + (price * tax_tate)
    global my_price
    print "my_price (inside function) =",my_price
    return total

my_price = float(raw_input("Enter a price:"))

totalPrice = calculateTax(my_price, 0.06)
print "price = ",my_price," Total price = ",totalPrice
print "my_price (outside function) =",my_price
