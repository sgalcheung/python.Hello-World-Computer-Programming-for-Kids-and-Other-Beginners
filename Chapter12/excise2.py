print "Enter 5 names:"
names = []
for i in range(0 ,5):
    names.append(raw_input())
snames = sorted(names)
print "The names are",
for name in names:
    print name,
print
print "The sorted names are",
for sname in snames:
    print sname,
