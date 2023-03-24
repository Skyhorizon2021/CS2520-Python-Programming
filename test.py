def firstDigit(n):
    while n > 10:
        n = n //10
    else:
        print ("First digit is",n)

def lastDigit(n):
    lastDigit = n % 10
    print("Last digit is",lastDigit)
def digits(n):
    count = 0
    while n > 1:
        count+=1
        n = n /10
    else:
        print("Number of digits is",count)
firstDigit(1729)
lastDigit(1729)
digits(1729)
    

