class Vector():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return "<"+str(self.x)+", "+str(self.y)+">" 
    def setX(self,value):
        self.x = value
    def setY(self,value):
        self.y = value
	
v1 = Vector(2,10)
print (v1) #will display <2, 10>  
v2 = Vector()
print(v2)  #will display <0, 0>
v2.setX(3)
v2.setY(5)
print(v2)   #now it will display <3, 5>