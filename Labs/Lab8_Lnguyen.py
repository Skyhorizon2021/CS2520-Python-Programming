#Name: Loc Nguyen
#Lab 8 Task 1
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
with open("text.txt","r") as textFile:
    content = textFile.readlines()
    for i in range(0,len(content)):
        if(i%2 == 0):
            print(content[i].rstrip())
        else:
            pass
print()
#print 2nd and 4th lines
with open("text.txt","r") as textFile:
    count=0
    for line in textFile:   
        count+=1
        if(count%2==0):
            print(line.rstrip())

#Lab 8 Task 2
#write strings one by one, i.e. write(str)
fp=open('data1.txt', 'w')
fp.write("hello\t")
fp.write("how are you")
fp.write("\n")
fp.write("thank you ")
fp.write("bye\n")
fp.close()

#print content
fp=open('data1.txt','r')
content1 = fp.read()
print("data1.txt\n" + content1)
fp.close()

#writelines(): write a sequence, i.e. a list or a tuple into a file
fp=open('data2.txt', 'w')
fp.writelines(["hello\t", "how are you", "\n", "thank you ", "bye\n"])
fp.close()

#print content
fp=open("data2.txt",'r')
content2 = fp.read()
print("data2.txt\n" + content2)
fp.close()

'''Output:
data1.txt
hello   how are you
thank you bye

data2.txt
hello   how are you
thank you bye
Comparison: THey have identical output despite using different methods'''

#Lab 8 Task 3
numList = []

fileNotFound=True
while fileNotFound:
    try:
        filename = input("Enter the name of file to open: ")
        file = open(filename,'r')
        print()
        for number in file:
            try:
                num = float(number)
                numList.append(num)
            except ValueError:
                numList.append(0.0)
        print(numList)               
        file.close()
        fileNotFound=False
        
    except FileNotFoundError:
        print("File not found.")
        fileNotFound=True

'''Output:
Enter the name of file to open: elevent.txt
File not found.
Enter the name of file to open: new.txt
File not found.
Enter the name of file to open: output.txt

[102.0, 20.5, 0.0, 0.0, 30.2, 7.0, 0.0, 93.0, 0.2, 3.0, 4.0, 7.0, 0.0, 0.0, 0.0, 78.0, 2312.123, 99.0, 2.0, 0.0]  
'''




