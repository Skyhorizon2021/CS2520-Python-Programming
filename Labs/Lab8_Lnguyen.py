#Name: Loc Nguyen
#Lab 7 Task 1
'''Objective: Use a text editor to type up a file with contents as follows and save as a .txt file.
We can’t touch
But we still reach out
We hunker down
But we still rise up
(1) Open the file and use readlines() to read in the text, and then display the 1st and 3rd lines,
close the file.
(2) Repeat the above and now use a for loop to read in the text, and then display the 2nd and 4th
lines, close the file. Note: you have to read in the whole file first, then display the 2 lines.
'''
#print 1st and 3rd lines
with open("C:/Users/locng/Documents/CS2520/CS2520-Python/Labs/text.txt","r") as textFile:
    content = textFile.readlines()
    for i in range(0,len(content)):
        if(i%2 == 0):
            print(content[i].rstrip())
        else:
            pass
print()
#print 2nd and 4th lines
with open("C:/Users/locng/Documents/CS2520/CS2520-Python/Labs/text.txt","r") as textFile:
    count=0
    for line in textFile:   
        count+=1
        if(count%2==0):
            print(line.rstrip())
