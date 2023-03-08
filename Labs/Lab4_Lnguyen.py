#Name: Loc Nguyen
#Lab 4 Task 1
import math

normSum=sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print(normSum)
floatSum=math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print(floatSum)
'''
0.9999999999999999
1.0
Both sum and fsum perform summation but fsum is specifically designed for
floating point arithmetic to avoid loss of precision. The difference comes from 
how numbers are converted to IEEE-754 when stored in memory
'''

#Lab 4 Task 2
def task2() :
    for i in range (8) :
        print(i, end = ' ')
print(task2())
'''Output
0 1 2 3 4 5 6 7 None
THe function doesn't return anything so None is returned when the function is called'''

#Lab 4 Task 3(a)
def fun (x=1,y=2,z):
    z = x + y
    y+=1
    return z*y
fun(x=1,y=2,z=9)
'''Error because the function has non-default argument of x and y assigned to value 1 and 2 respectively
while z follows default argument.'''
#Lab 4 Task 3(b)
def hoho(x,y=2,z=1):
    z=x+z
    y+=1
    return z*y
print(hoho(5))
'''Result 18'''
print(hoho(6,z=3,y=1))
'''Result 18'''

#Lab 4 Task 4
def main():
    x,y=3,4
    x,y=swap(x,y)
    print(x,y)
def swap(a,b):
    return b,a
main()
'''Revised Code is above
The problem with the old code is that the swap function only swap values inside the function
and not the values calling the function. You have to add x,y = swap(x,y) to store the swap values '''

#Lab 4 Task 5
a, b = 0, 5
def main() :
    global a, b
    i = 10
    b = g(i)
    print(a+b+i)
def f(i) :
    n=0
    while n*n <= i:
        n = n + 1
    return n-1
def g(a) :
    b=0
    for n in range(a):
        i = f(n)
        b = b+i
        return b
main()
'''
a and b are global variable and the remaining variables are local
Guess output = 50
Actual output 10
'''

