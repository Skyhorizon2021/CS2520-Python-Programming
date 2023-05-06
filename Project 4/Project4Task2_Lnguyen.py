#Name: Loc Nguyen
#Date: 05/05/2023
'''Objective:A Polygon class has a private data element pointList, e.g. [(0, 0), (0, 5), (3, 2)], an addPoint method, a
getPoint method, displaySide() method – how many sides for this polygon, and a draw method (note:
using above 3 points you can draw a triangle, e.g. draw a line from (0, 0) to (0, 5), a line from (0, 5) to (3,
2), and a line from (3, 2) to (0, 0).)
A Rectangular class inherits from the Polygon class with two new data members, lowerleft and
upperRight, and two new methods getLowerLeft() and getUpperRight().
Main function and test run: (1) create a pentagon object, display the # of sides, and draw it; (2) create a
rectangle object, display the LowerLeft and UpperRight points, display the # of sides, and draw it.
Note: may use Turtle to draw; may change the requirements slightly to introduce your own features (e.g.
methods, data members etc.)'''

import turtle

class Polygon:
    def __init__(self,list=[]) -> None:
        self.list = list
    def addPoint(self,point):
        self.point = point
        self.list.append(self.point)
    #get the coordinate of a point based on the index
    def getPoint(self,index):
        return self.list[index]
    def displaySide(self):
        print("This polygon has",len(self.list),"sides")
    def draw(self):
        #setup Turtle
        pen = turtle.Turtle()
        screen = turtle.Screen()
        screen.title("Polygon")
        screen.screensize(800,500,bg="black")

        pen.hideturtle()
        pen.pencolor("white")
        pen.speed(1)
        
        for sides in range(len(self.list)):
            start = self.getPoint(sides)
            #get the next point unless the start is the last point, then get the origin as the destination
            try:
                dest = self.getPoint(sides+1)
            except:
                dest = self.getPoint(0)
            pen.pu()
            pen.goto(start)
            pen.pd()
            pen.goto(dest)
        
            
#class Rectangle inherit Polygon
class Rectangle(Polygon):
    def __init__(self,list=[]) -> None:
        super().__init__(list)
    def getLowerLeft(self):
        self.lowerLeft = self.list[0]
        return self.lowerLeft
    def getUpperRight(self):
        self.upperRight = self.list[2]
        return self.upperRight
    #define the turtle to finish after drawing the rectangle
    def draw(self):
        super().draw()
        turtle.done()

#class Pentagon inherit Polygon
class Pentagon(Polygon):
    def __init__(self, list=[]) -> None:
        super().__init__(list)

def main():
    #defint private data element pointlist
    __pointList = Polygon([(0,0),(0,50),(30,20)])
    #define private pentagon object and pass argument to it
    __pentagon = Pentagon([(0,0),(0,50),(50,50),(50,0),(25,-25)])
    __pentagon.displaySide()
    __pentagon.draw()

    #define private rectangle object and pass argument to it
    __rectangle = Rectangle([(200,200),(200,300),(325,300)])
    __rectangle.addPoint((325,200))
    __rectangle.displaySide()
    print("Lower left point is",__rectangle.getLowerLeft())
    print("Upper right point is",__rectangle.getUpperRight())
    __rectangle.draw()

main()
'''Output:
This polygon has 5 sides
This polygon has 4 sides
Lower left point is (200, 200)
Upper right point is (325, 300)
'''


