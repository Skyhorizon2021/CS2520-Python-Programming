#Task 1
def firstDigit(num):
    #Divide by 10 until less than 1 and then extract the number that's between 1 and 10
    while num > 1:
        num /= 10
    if num < 1:
        num*=10
        num//1
    return 
def lastDigit(num):
    #Divide by 10 and subtract by the rounded version to extract the decimal value then multiple by 5
    return DigitLast
def digits(num):
    #divide by 10 and count how many times before less than 1
    counter=0
    while num > 1:
        num /= 10
        counter+=1
    return counter
def main():
    num=int(input("Please enter an integer: "))
    print(firstDigit(num))
    print(lastDigit(num))
    print(digits(num))

main()

#Task 2
def getSum(positiveNum):
    for i in range(positiveNum-2):
        total=0
        total+=(positiveNum+1)**2
        positiveNum-=1
    return total 

repeat=True
while repeat:
    positiveNum=int(input("Enter a positive number: "))
    if positiveNum <= 0:
        repeat=False
        break
    else:
        print(getSum(positiveNum))
        

        