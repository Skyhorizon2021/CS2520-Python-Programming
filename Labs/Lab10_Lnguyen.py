#Name: Loc Nguyen
#Date: 04/21/2023
'''Objective: Convert java code to python code'''

class Bicyble:
    def __init__(self,gear,speed):
        self.gear = gear
        self.speed = speed
    def applyBrake(self,decrement):
        self.speed -= decrement
    def speedUp(self,increment):
        self.speed += increment
    def __str__(self):
        return ("No of gears are " + self.gear + "\n" + "speed of bicycle is " + self.speed)

#class mountain bike is a subclass of Bicycle
class MountainBike(Bicyble):
    #add seat height as a field
    def __init__(self, gear, speed, startHeight):
        #inherit gear and speed from Bicycle
        super().__init__(gear, speed)
        self.seatHeight = startHeight
    def setHeight(self,newValue):
        self.seatHeight = newValue
    


        
        
