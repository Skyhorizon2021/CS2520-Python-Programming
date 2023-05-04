import turtle
import time
import random

pen = turtle.Turtle()
screen = turtle.Screen()
screen.title("Asteroid")
screen.screensize(800,500,bg="black")

pen.hideturtle()
pen.pencolor("white")

x=0
y=0
pen.speed(0)
pen.penup()
pen.goto(0,200)
pen.pendown()

#create asteroid
while True:
    pen.forward(x)
    pen.right(y)
    x+=3
    y+=1
    if y==210:
        break
    

#create stars 
pen.pencolor("white")
def star():
    for i in range(5):
        pen.pendown()
        pen.forward(20)
        pen.right(144)
#define range of color        
screen.colormode(255)
count=0
while True:
    x = random.randint(-400,250)
    y = random.randint(-400,250)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    #randomize pen color
    pen.pencolor(r,g,b)
    pen.penup()
    pen.goto(x,y)
    star()
    count+=1
    if count>200:
        break    

turtle.done()

