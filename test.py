#Task 2
import turtle


screen = turtle.Turtle()
pen = turtle.pen()

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
    __pointList = Polygon([(0,0),(0,5),(3,2)])
    __pointList.displaySide()

main()