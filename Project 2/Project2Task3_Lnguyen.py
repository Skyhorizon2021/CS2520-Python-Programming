#Name: Loc Nguye
#Project 2 Task 3
'''Objective: Write a program that asks the user to enter a zip code (in ZIP+4 format) then encode the 
zip code and use turtle module to draw the barcode (note: this is the old format barcode.)'''
import turtle

#set up turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")

#setup screen
screen = turtle.Screen()
screen.title("Zipcode Visualization")
screen.screensize(800,500,bg="white")
#turtle var
distance=10
angle=90
longBar = 50
shortBar = 25
#change starting coordinate
pen.pu()
pen.left(angle*2)
pen.forward(distance*30)
pen.right(angle*2)

#find the sum of digit by modulus. Ensure num is an int by casting
def getSum(num):
    sum = 0
    while (num != 0):
        sum =sum + int(num % 10)
        num = int(num/10)
    return sum
#convert digit into code
def conversion(num):
    match num:
        case 0:
            code='11000'
        case 1:
            code='00011'
        case 2:
            code='00101'
        case 3:
            code='00110'
        case 4:
            code='01001'
        case 5:
            code='01010'
        case 6:
            code='01100'
        case 7:
            code='10001'
        case 8:
            code='10010'
        case 9:
            code='10100'
    return code
def draw(code):
    if code =='1':
        #draw longbar
        pen.pd()
        pen.left(angle)
        pen.forward(longBar)
        pen.pu()
        #reposition pen for next run
        pen.right(angle)
        pen.forward(distance)
        pen.right(angle)
        pen.forward(longBar)
        pen.left(angle)
    else:
        #draw shortbard
        pen.pd()
        pen.left(angle)
        pen.forward(shortBar)
        pen.pu()
        #reposition pen for next run
        pen.right(angle)
        pen.forward(distance)
        pen.right(angle)
        pen.forward(shortBar)
        pen.left(angle)
        
            
#get zipcode and replace hyphen
zipCode = input("Enter your zip code (in ZIP+4 format): ")
#Simple error checking
if len(zipCode)!=10:
    exit("Invalid zipcode")
#remove hyphen
zipCode=zipCode.replace('-','')
#cast zipcode to int
intZipCode=int(zipCode)
#get the total of digits
total=getSum(intZipCode)
#find checkSum digit
checkSumDigit=10 - (total%10)
#append checkSum digit to zipcode and store in modCode
modCode=str(zipCode)+str(checkSumDigit)

print("Modified zipcode:",modCode)

barCode=''
#convert value to binary and match case to ever
for index in modCode:
    digitBarcode=conversion(int(index))
    barCode=barCode + digitBarcode
print("Barcode for this zipcode:",barCode)
#draw start
draw('1')
#feed digit by digit into draw function to draw
for index in barCode:
    draw(index)
#draw stop
draw('1')
turtle.done()
'''Output
Test(1)
Enter your zip code (in ZIP+4 format): 55555-1237
Modified zipcode: 5555512372
Barcode for this zipcode: 01010010100101001010010100001100101001101000100101
Test(2)
Enter your zip code (in ZIP+4 format): 91768-1111
Modified zipcode: 9176811115
Barcode for this zipcode: 10100000111000101100100100001100011000110001101010
Test(3)
Enter your zip code (in ZIP+4 format): 928001-1212
Invalid zipcode
'''
