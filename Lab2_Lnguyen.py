#Name: Loc Nguyen
#Lab 2 - Task 1
#Date - 02/06/2023
#Objective - Compute FV based on user input of PV, INT, and YRS

PV = float(input("Enter the present value: "))
INT = float(input("Enter the interest rate: "))
YRS = float(input("Enter the number of years: "))
FV = PV * (1.0+INT/100)**YRS
print("The future value is %.2f" % FV )

'''
Test(1)
Enter the present value: 1000.0
Enter the interest rate: 5.0
Enter the number of years: 30
The future value is 4321.94
Test(2)
Enter the present value: 1530.50
Enter the interest rate: 3.5
Enter the number of years: 15
The future value is 2564.12
'''

#Lab 2 - Task 2 part a 
#Objective - Convert Java code to Python
v1,v2,v3 = 5,2,1
v1 += 1
v3 += v1*v2
v2 -= 1
print("v1=%d\tv2=%d\tv3=%d" % (v1,v2,v3))
'''Output
v1=6    v2=1    v3=13
'''

#Lab 2 - Task 2 part b
'''Objective - Enter three integer values for three variables first, second, and third, write one Python 
assignment statement (note: only one statement allowed) that swaps the three values 
such that first will get second’s value, second gets first’s value and third gets first’s 
(original) value, i.e. if enter three values first = 5, second = 7, third = 2, after swap, first = 
7, second = 2, and third = 5.'''
var1 = int(input("Enter the first number: "))
var2 = int(input("Enter the second number:"))
var3 = int(input("Enter the third number: "))

var1,var2,var3 = var2,var3,var1
print("After swapping,\nVariable 1 is %d\nVariable 2 is %d\nVariable 3 is %d" % (var1,var2,var3))
'''Ouput
After swapping,
Variable 1 is 7
Variable 2 is 2
Variable 3 is 5'''

#Lab 2 - Task 3
'''Objective - Convert Java code to Python'''
num1=int(input("Enter value for num 1: "))
num2=int(input("Enter value for num 2: "))
quotient=num1//num2
remainder=num1%num2
print("Quotient when %d/%d is: %d" % (num1,num2,quotient))
print("Remainder when %d is divided by %d is %d" % (num1,num2,remainder))
'''Output
Test(1)
Enter value for num 1: 12
Enter value for num 2: 35
Quotient when 9/3 is: 0
Remainder when 9 is divided by 3 is 12
Test(2)
Enter value for num 1: 35
Enter value for num 2: 13
Quotient when 35/13 is: 2
Remainder when 35 is divided by 13 is 9
'''