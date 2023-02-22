#Name: Loc Nguyen
#Lab 1 - Task 2
#Objective: Print out how much a user needs to pay based on units purchased
hour = 2
minute = 15
second = 10
formatStr = “{1} : {2} : {0}“
print(formatStr.format(hour, minute, second))
print("Welcome to Soda Machine")
print("Alvin's purchase: ")
eachCan = 5     #5 dollars for each can
numOfCans = 3      #numOfCans 3 cans
print("Alvin needs to pay", eachCan * numOfCans, "dollars")

print("\nNow Terri is using the machine: ")
eachCan = int(input("Please enter the unit price: "))
numOfCans = int(input("How many cans did you buy? "))
print("Terri needs to pay", eachCan * numOfCans, "dollars")

'''File Output

Welcome to Soda Machine
Alvin's purchase:
Alvin needs to pay 15 dollars

Now Terri is using the machine:
Please enter the unit price: 10
How many cans did you buy? 5
Terri needs to pay 50 dollars
'''