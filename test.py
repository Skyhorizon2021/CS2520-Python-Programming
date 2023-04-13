t = set()
print(type(t))
t.update("1","2","3")
print(t)
for element in t:
    print(element,end="\n")