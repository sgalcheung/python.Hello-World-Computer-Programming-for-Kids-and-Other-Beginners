import easygui

easygui.msgbox("This program converts Fahrenheit to Celsius")
fahr = float(easygui.enterbox("Type in atemperature in Fahrenheit:"))
cel = 5 / 9.0 * (fahr - 32)
easygui.msgbox("This is " + str(cel) + " degress Celsius.")
