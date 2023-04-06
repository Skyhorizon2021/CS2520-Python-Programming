infile = open("output.txt", "r")   #line 1
word = infile.readline()   #line 2
word = word.rstrip()  #line 3
word = int(word)
total = sum(word)   #line 4
print(total)   