# -*- coding: cp936 -*-
length = float(raw_input("请输入房间的长："))
width = float(raw_input("请输入房间的宽："))
price = float(raw_input("请输入每平方尺地毯的价格："))
areaM = length * width
areaC = areaM * 9
totalPrice = areaC * price
print "总共需要",areaM,"平方米地毯"
print "总共需要",areaC,"平方尺地毯"
print "地毯总价格",totalPrice
