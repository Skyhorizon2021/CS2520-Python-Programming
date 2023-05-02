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
print("Doubled list:",list(map((lambda val: val*2),L)))
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
    



