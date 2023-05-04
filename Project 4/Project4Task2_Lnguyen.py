#Task 2
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
        return self.lowerLeft
    def getUpperRight(self):
        return self.upperRight
    def draw(self):
        super().draw()

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
    __rectangle = Rectangle([],(0,0),(125,100))

    __rectangle.displaySide()
    print("Lower left point is",__rectangle.getLowerLeft())
    print("Upper right point is",__rectangle.getUpperRight())
    __rectangle.draw()


    

main()


