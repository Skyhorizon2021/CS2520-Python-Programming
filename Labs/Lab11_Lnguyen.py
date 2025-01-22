#Name: Loc Nguyen
#Date: 04/27/2023
#Task 1
'''Objective: 
(5 pts) Write a general sort function that takes a comparison function as well as a list of values
as parameters, then sort the list according to the comparison function provided. May use any
sorting algorithm but do NOT use any predefined sorting function. Test the following:
(1) Sort the integer list [5, 2, 12, 4, 9, 13, 22, 1, 6, 17] to descending order
(2) Sort the name list ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob",
"Joy"] according to alphabetical order.
(3) Sort the tuple list of (name, count) according to name’s alphabetical order. If same name,
then the one has higher count listed first. [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1),
("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)].
'''
#comparison functions
#descending order algorithm for list
def descend(x,y):
    return x > y

#ascending alpha order algo for list
def ascend(x,y):
    return x < y

#sort ascending alpha with higher count for secondary criteria 
#since each tuple is getting passed as an argument, check if it's the same
#If not, compare the second element in the tuple. Else, return the boolean
def tupleSort(x,y):
    if x == y:
        return x[1] > y[1]
    return x[0] < y[0]
#generalSorter is a higher order function bc it takes a comparison function as arg
def generalSorter(data,compFunc):
    for i in range(len(data)):
        for j in range(len(data)):
            if compFunc(data[i],data[j]):
                data[i],data[j] = data[j],data[i]
    return data
  

def main():
    #passing the data and the function into the sort function to sort the data list accordingly
    intList = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
    intListSort = generalSorter(intList,descend)
    print("Integer list:",intListSort)
    nameList = ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"] 
    nameListSort = generalSorter(nameList,ascend)
    print("Name list:",nameListSort)
    tupleList = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]
    tupleListSort = generalSorter(tupleList,tupleSort)
    print("Name & count list:",tupleListSort)
#execute    
main()
'''Output:
Integer list: [22, 17, 13, 12, 9, 6, 5, 4, 2, 1]
Name list: ['Alp', 'Alpine', 'Beta', 'Bob', 'Jolly', 'Joy', 'Kate', 'Kate', 'Sam', 'Samuel']
Name & count list: [('Alp', 2), ('Alp', 1), ('Alpine', 2), ('Beta', 3), ('Bob', 2), ('Jolly', 1), ('Kate', 3), ('Kate', 5), ('Sam', 4), ('Sam', 2), ('Sam', 3)]'''

#Task 2
'''Objective: (5 pts) Use list comprehension to create a list L with 100 elements from 1 to 100 in order, then
use map and/or filter functions to perform the following – note: For each case, in main function,
print L first, then for each function called, print out the result.
(1) Return a list with each element is a doubled value of corresponding element of L. (must use
lambda expression.)
(2) Return a list with each element a squared value of each odd element in L. (your choice of
using or not using a lambda expression.)
(3) Return a list by taking all prime members from L. An isPrime() function is attached for your
reference'''
#create a list with list comprehension
L = [i for i in range(1,101)]
#function to print double val
print("Doubled list:",list(map(lambda val: val*2,L)))
#function to print a squared value of odd element in L 
def squareOdd(x):
    return x**2
#filter and only get odd number, then map it and print it
oddList = list(filter((lambda num:num%2==1),L))
print("Squared odd list:",list(map(squareOdd,oddList)))
#function to get prime number
from math import sqrt
def isPrime(num):
    if num<=1:
        return 0
    for fac in range(2,int(sqrt(num))+1):
        if num%fac==0:
            return 0
    return 1
primeList = list(filter(isPrime,L))
print("Prime list:",primeList)
'''Output:
Doubled list: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]
Squared odd list: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249, 3481, 3721, 3969, 4225, 4489, 4761, 5041, 5329, 5625, 5929, 6241, 6561, 6889, 7225, 7569, 7921, 8281, 8649, 9025, 9409, 9801]     
Prime list: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]'''



