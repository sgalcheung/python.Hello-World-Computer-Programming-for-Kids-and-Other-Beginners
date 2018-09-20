def printAddr (name, num ,str, city, prov ,pcode, country):
    print name
    print num,
    print str
    print city,
    if prov != "":
        print ", "+prov
    else:
        print ""
    print pcode
    print country
    print

printAddr("tom","43","Main St.","Caton","Guangdong","110011","China")
printAddr("jack","22","2nd Ave.","Hong Kong","","23456","China")
