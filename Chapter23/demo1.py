from random import *

coin = ["Heads", "Tails"]
heads_in_row = 0;
ten_heads_in_row = 0
for i in range (1000000):
	if choice(coin) == "Heads":
		heads_in_row += 1
	else:
		heads_in_row = 0

	if heads_in_row == 10:
		ten_heads_in_row += 1
		heads_in_row = 0

print "We got 10 heads in a row", ten_heads_in_row, "times."