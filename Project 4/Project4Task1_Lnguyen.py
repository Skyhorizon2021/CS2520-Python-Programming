class Pair:
    #constructor 
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
    #overloading +,*, and / operator
    def __add__(self,other):
        return Pair(self.x+other.x,self.y+other.y)
    def __mul__(self,other):
        return Pair(self.x*other.x,self.y*other.y)
    #use truediv to overload /, div will only overload // automatically
    def __truediv__(self,other):
        return Pair(self.x*self.y-other.x*other.y,self.x*other.y-self.y*other.y)
    #define string method to print
    def __str__(self) -> str:
        return ("<"+str(self.x)+","+str(self.y)+">")

def main():
    #Test case 1
    print("Test run 1")
    p1 = Pair(3,2)
    p2 = Pair(1,5)
    p3 = Pair(4,3)
    result1 = p1+p2
    result2 = p1*p2
    result3 = p1/p2
    result4 = p1+p2*p3
    result5 = p1*p2/p3+p1
    #display result
    print("p1 =",p1)
    print("p2 =",p2)
    print("p3 =",p3)
    print("Result 1 =",result1)
    print("Result 2 =",result2)
    print("Result 3 =",result3)
    print("Result 4 =",result4)
    print("Result 5 =",result5)

    #Test case 2
    print("Test run 2")
    p1 = Pair(10,2)
    p2 = Pair(3,4)
    p3 = Pair(9,5)
    result1 = p1+p2
    result2 = p1*p2
    result3 = p1/p2
    result4 = p1+p2*p3
    result5 = p1*p2/p3+p1
    #display result
    print("p1 =",p1)
    print("p2 =",p2)
    print("p3 =",p3)
    print("Result 1 =",result1)
    print("Result 2 =",result2)
    print("Result 3 =",result3)
    print("Result 4 =",result4)
    print("Result 5 =",result5)
    
main()
'''Output:
Test run 1
p1 = <3,2>
p2 = <1,5>
p3 = <4,3>
Result 1 = <4,7>
Result 2 = <3,10>
Result 3 = <1,5>
Result 4 = <7,17>
Result 5 = <21,-19>
Test run 2
p1 = <10,2>
p2 = <3,4>
p3 = <9,5>
Result 1 = <13,6>
Result 2 = <30,8>
Result 3 = <8,32>
Result 4 = <37,22>
Result 5 = <205,112>
'''
