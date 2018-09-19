print "Enter 5 names:"
names = []
for i in range(0, 5):
    names.append(raw_input())
print "The names are",
for name in names:
    print name,
print
print "Replace one name. Which one? (1-5):",
index = int(raw_input())
newName = raw_input("New name:")
names[index-1] = newName
print "The names are",
for nname in names:
    print nname,
