#Name: Loc Nguyen
#Date: 03/08/2023
#Lab 6 Task 1
'''Objective
1. Prompt user to enter a sentence, e.g. “Good morning CS2520”
2. Split the string into a sequence, e.g. [‘Good’, ‘morning’, ‘CS2520’]
3. Concatenate each word in the sequence by inserting a special character (e.g. ‘#’) between them, e.g. 
Good#morning#CS2520 '''
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
'''Objective
1. Create List 1. Enter elements one by one. The list size can be determined by user, i.e. enter a special 
symbol as an end marker to stop the input process.  E.g. [5, 2, 21, 23, 13, 17, 8, 1, 12, 45]
2. Create List 2. Use list comprehension to create a list with 20 elements randomly generated in the 
range of [0, 50].
3. Find the last element of the first list and then reverse the list.
4. Combine the two lists (original List 1 and List 2) and then sort the list in descending order.'''
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

'''Lab 6 Task 3
Objective:
1. Given a tuple of names, say (“Winny”, “Ada”, “Lev”, “Kay”, “Jack”, “Sam”, “Mark”), and a list of ages, 
e.g. [20, 18, 22, 16, 20, 18, 18], use zip feature to form a tuple of tuples, i.e.  ((“Winny”, 20), (“Ada”, 18), 
(“Lev”, 22), (“Kay”, 16), (“Jack”, 20), (“Sam”, 18), (“Mark”, 18))
2. From the tuple of (name, age), find the name who is the youngest as well as the average age.
3. Sort the tuple into the descending order of the scores. If score is same, arrange the tuples in 
alphabetical order of names. E.g. the above should be: ((‘Lev, 22), (‘Jack’, 20), (‘Winny’, 20), ...)'''
#initilize var
sum = 0
count = 0
#sort by 2nd element
def sortTuple(tup):
    ascSort=sorted(tup,key = lambda x: x[1])
    return ascSort
#reverse sort by 2nd element and alphabetically by 1st element 
def reverseSortTuple(tup):
    desSort=sorted(tup,key = lambda x: (-x[1],x[0]))
    return desSort
#initialize tuples and zip them
t1 = ("Winny","Ada","Lev","Kay","Jack","Sam","Mark")
t2 = (20,18,22,16,20,18,18)
t3 = zip(t1,t2)
sort_Tuple = sortTuple(tuple(t3))
minPair = sort_Tuple[0]

#assign age and name value
minName = minPair[0]
minAge = minPair[1]

#sort in descending order
revSort_Tuple = reverseSortTuple(sort_Tuple)
#get sum
for i in sort_Tuple:
    sum += i[1]
    count += 1

#calculate average age
avgAge = sum / count

print("Tuple in descending order",revSort_Tuple)
print("Average age is %.2f" % avgAge)
print("The youngest is",minName,"at",minAge,"years old")

#reinitialize var
sum = 0
count = 0
#second test pair
t4 = ("Psaki","Yuki","Lelouch vi Britannia","Zero","Bald Cape","Hinata","Shinichi","Doyle")
t5 = (15,6,20,20,31,14,7,49)
t6 = zip(t4,t5)
sort_Tuple = sortTuple(tuple(t6))
minPair = sort_Tuple[0]

#assign age and name value
minName = minPair[0]
minAge = minPair[1]

#sort in descending order
revSort_Tuple = reverseSortTuple(sort_Tuple)
#get sum
for i in sort_Tuple:
    sum += i[1]
    count += 1

#calculate average age
avgAge = sum / count

print("Tuple in descending order",revSort_Tuple)
print("Average age is %.2f" % avgAge)
print("The youngest is",minName,"at",minAge,"years old")
'''Output
Test(1)
Tuple in descending order [('Lev', 22), ('Jack', 20), ('Winny', 20), ('Ada', 18), ('Mark', 18), ('Sam', 18), ('Kay', 16)]
Average age is 18.86
The youngest is Kay at 16 years old
Test(2)
Tuple in descending order [('Doyle', 49), ('Bald Cape', 31), ('Lelouch vi Britannia', 20), ('Zero', 20), ('Psaki', 15), ('Hinata', 14), ('Shinichi', 7), ('Yuki', 6)]
Average age is 20.25
The youngest is Yuki at 6 years old'''


   