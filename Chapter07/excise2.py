sex = raw_input("Please input your gender.(man:m;feman:f)")
if sex == "f":
    age = int(raw_input("Please input your age."))
    if 10 <= age <= 12:
        print "Congratulations on joining our team."
    else:
        print "Sorry, your age is not within our requirement."
else:
    print "Sorry, we only recruit female players."
