#Name: Loc Nguyen
#Date: 03/08/2023
#Lab 6 Task 1

userInput= input("Please enter a sentence: ")
userInput=userInput.split(' ')
concatStr = ''
for i in userInput:
    concatStr=concatStr+i+'#'
print("Final result:",concatStr)
'''Output
Test(1)
Please enter a sentence: Good morning CS2520
Final result: Good#morning#CS2520#
Test(2)
Please enter a sentence: The past is nostalgic 
The future is hopeful The present is a gift
Final result: The#past#is#nostalgic#The#future#is#hopeful#The#present#is#a#gift#
'''

#Lab 6 Task 2
import random
intList1 = []
repeat=True
while repeat:
    userInput=input("/List 1/Enter an integer (q to finish): ")
    if userInput=='q':
        repeat=False
    else:
        intList1.append(int(userInput))
intList2=[] 

counter=0
while counter<20:
    intList2.append(random.randint(0,50))
    counter+=1
#print last element
print("Last element of list 1 is",intList1[len(intList1)-1])
#reverse List 1 then print
intList1.sort(reverse=True)
print("List 1 reversed:",intList1)
#combine list 1 and 2, reverse sort, then print
totalList=intList1+intList2
totalList.sort(reverse=True)
print("Both lists sorted in descending order:",totalList)
'''Output
Test(1)
/List 1/Enter an integer (q to finish): 5
/List 1/Enter an integer (q to finish): 2
/List 1/Enter an integer (q to finish): 21
/List 1/Enter an integer (q to finish): 23
/List 1/Enter an integer (q to finish): 13
/List 1/Enter an integer (q to finish): 17
/List 1/Enter an integer (q to finish): 8
/List 1/Enter an integer (q to finish): 1
/List 1/Enter an integer (q to finish): 12
/List 1/Enter an integer (q to finish): 45
/List 1/Enter an integer (q to finish): q
Last element of list 1 is 45
List 1 reversed: [45, 23, 21, 17, 13, 12, 8, 5, 2, 1]
Both lists sorted in descending order: [49, 45, 45, 44, 43, 38, 38, 37, 36, 36, 34, 28, 27, 23, 21, 17, 13, 12, 12, 11, 11, 8, 5, 5, 5, 5, 3, 2, 2, 1]
Test(2)
/List 1/Enter an integer (q to finish): 12
/List 1/Enter an integer (q to finish): 78
/List 1/Enter an integer (q to finish): 98
/List 1/Enter an integer (q to finish): 5
/List 1/Enter an integer (q to finish): 1
/List 1/Enter an integer (q to finish): 0
/List 1/Enter an integer (q to finish): 5
/List 1/Enter an integer (q to finish): 45 
/List 1/Enter an integer (q to finish): 6
/List 1/Enter an integer (q to finish): 123
/List 1/Enter an integer (q to finish): q
Last element of list 1 is 123
List 1 reversed: [123, 98, 78, 45, 12, 6, 5, 5, 1, 0]
Both lists sorted in descending order: [123, 98, 78, 50, 49, 45, 45, 44, 42, 41, 33, 30, 29, 28, 26, 25, 22, 19, 19, 18, 15, 15, 14, 12, 11, 6, 5, 5, 1, 0]'''

   