#Task 2
import turtle

class Polygon:
    def __init__(self,list) -> None:
        self.list = list
    def addPoint(self):
        pass
    def getPoint(self):
        pass
    def displaySide(self):
        print("This polygon has",len(self.list),"sides")
    def draw(self):
        pass



def main():
    #setup Turtle
    screen = turtle.Screen()
    pen = turtle.Turtle()
    screen.title("Polygon")
    screen.screensize(800,500,bg="black")

    pen.hideturtle()
    pen.pencolor("white")

    pen.speed(5)
    #define private pointList object and pass argument to it
    __pointList = Polygon([(0,0),(0,5),(3,2)])
    __pointList.displaySide()

main()


