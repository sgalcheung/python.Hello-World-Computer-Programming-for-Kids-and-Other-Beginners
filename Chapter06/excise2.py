import easygui

name = easygui.enterbox("What is your name?")
addr = easygui.enterbox("What is your street address?")
city = easygui.enterbox("What is your city?")
state = easygui.enterbox("What is your state or province?")
code = easygui.enterbox("What is your postal code or zip code?")

whole_addr = name + "\n" + addr + "\n" + city + "\n" + state + "\n" + code

easygui.msgbox(whole_addr,"Here is your address:")
