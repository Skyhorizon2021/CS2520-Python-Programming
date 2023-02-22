#Name: Loc Nguyen
#Date: 02/08/2023

#Lab 3 Task 1
'''Objective - Write code to enter three values, write one if statement (could use if-elif-else) to find 
the largest of the three values. Do three test runs: (1) enter three strings “hello”, “how’re you”, “hoho”; 
(2) enter three integer numbers 420, 351, 530; (3) enter three float numbers: -35.8, -28, -36.5
Your code for entering values may look like: '''

testRun = int(input("Please enter the type of input: 1 for integer, 2 for float, and 3 for string: "))
#conversion of data types
if testRun==1:
    firstVal = int(input("Please enter the first value: "))
    secondVal = int(input("Please enter the second value: "))
    thirdVal = int(input("Please enter the third value: "))
elif testRun==2:
    firstVal = float(input("Enter a number: "))
    secondVal = float(input("Enter a number: "))
    thirdVal = float(input("Enter a number: "))
elif testRun==3:
    firstVal = input("Please enter the first value: ")
    secondVal = input("Please enter the second value: ")
    thirdVal = input("Please enter the third value: ")
else:
    pass
#code for find the largest
if firstVal>secondVal and firstVal>thirdVal:
    print("The largest value is", firstVal)
elif secondVal>firstVal and secondVal>thirdVal:
    print("The largest value is", secondVal)
elif thirdVal>firstVal and thirdVal>secondVal:
    print("The largest value is", thirdVal)
else:   
    print("One or more values may be equal to another value")
'''Output
Test(1)
Please enter the first value: hello 
Please enter the second value: how're you
Please enter the third value: hoho
Please enter the type of input: 1 for integer, 2 for float, and anything for string: d
The largest value is how're you
Test(2)
Please enter the first value: 420
Please enter the second value: 351
Please enter the third value: 530
Please enter the type of input: 1 for integer, 2 for float, and anything for string: 1
The largest value is 530
Test(3)
Please enter the type of input: 1 for integer, 2 for float, and 3 for string: 2
Enter a number: -35.8
Enter a number: -28
Enter a number: -36.5
The largest value is -28.0
'''

#Lab 3 Task 2
#Objective - Convert if-else into conditional print expression
count = int(input("Please enter the number of items purchased: "))
total = int(input("Please enter the total cost: "))
print("Average =" ,0 if count==0 else total/count)
'''Output
Test(1) Zero count
Please enter the number of items purchased: 0
Please enter the total cost: 0
Average = 0
Test(2) Non-zero count
Please enter the number of items purchased: 10
Please enter the total cost: 45
Average = 4.5
'''

#Lab 3 Task 3 (a)
#Objective - Guessing code output
j=1
while j < 10 :
      j += 2
      if j == 5 :
            continue
      print(j, end =  " ") 
'''
Guessed output(a)
3 7 9 11
Actual Output(a)
3 7 9 11
'''

#Lab 3 Task 3 (b)
#Objective - Guessing code output
for j in range (50) :
    j += 2
    print(j, end =  " ")
    if j == 15 :
        break
'''
Guessed Output(a)
2 3 4 5 6 7 8 9 10 11 12 13
Actual Output(b)
2 3 4 5 6 7 8 9 10 11 12 13 14 15 
Note - changing variable value in code body doesn't affect counter when using for j in range
'''

#Lab 3 Task 4
#Objective - Check if a number is prime or not
num=int(input("Enter an integer to check Prime or Not: "))
i,count = 2,0
while(i <= num/2):
    if(num % i ==0):
        count+=1
        break
    i+=1
if count==0:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
'''Output
Test(1)
Please enter a number to check Prime or Not: 71
71 is a prime number
Test(2)
Please enter a number to check Prime or Not: 119
119 is not a prime number
Test(3)
Please enter a number to check Prime or Not: 113
113 is a prime number
Test(4)
Please enter a number to check Prime or Not: 1124
1124 is not a prime number
Test(5)
Please enter a number to check Prime or Not: 91
91 is not a prime number'''    




    

