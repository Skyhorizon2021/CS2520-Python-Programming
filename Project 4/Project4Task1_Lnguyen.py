#Name: Loc Nguyen
#Date: 05/05/2023
'''Objective:
(1) Define a Pair class that consists of two elements, i.e. a Pair object has two members x, y as well
as a number of methods described below.
(2) Define a constructor that creates a Pair object. The default value for x, y are 0 and 0;
(3) Define a __str__ method, so if p is a Pair object, print(p) will display in the form of <x, y>;
(4) Use operator overloading to define the +, *, and / operators. These operators are defined as
follows -- assume p1 = Pair(x1, y1), p2 = Pair(x2, y2)
p1 + p2 => <x1 + x2, y1+y2> #here => means “defined as”
p1 * p2 => <x1*x2, y1*y2>
p1 / p2 => <x1*y1-x2*y2, x1*x2 – y1*y2>
(5) Write a main function to test your code. You need to include two test runs, the requirement for
the first test run is shown below while you create the other of test run to properly test all above
functions.
Test run: Create three Pair objects with p1 referring to <3, 2>, p2 referring to <1, 5>, p3
referring to <4, 3>; perform p1 + p2, p1 * p2, p1/p2, p1 + p2 * p3, and p1 * p2 / p3 + p1; display
p1, p2, p3 as well as the operation results.'''

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
    print("Result of p1+p2 =",result1)
    print("Result of p1*p2 =",result2)
    print("Result of p1/p2 =",result3)
    print("Result of p1+p2*p3 =",result4)
    print("Result of p1*p2/p3+p1 =",result5)

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
    print("Result of p1+p2 =",result1)
    print("Result of p1*p2 =",result2)
    print("Result of p1/p2 =",result3)
    print("Result of p1+p2*p3 =",result4)
    print("Result of p1*p2/p3+p1 =",result5)
    
main()
'''Output:
Test run 1
p1 = <3,2>
p2 = <1,5>
p3 = <4,3>
Result of p1+p2 = <4,7>
Result of p1*p2 = <3,10>
Result of p1/p2 = <1,5>
Result of p1+p2*p3 = <7,17>
Result of p1*p2/p3+p1 = <21,-19>
Test run 2
p1 = <10,2>
p2 = <3,4>
p3 = <9,5>
Result of p1+p2 = <13,6>
Result of p1*p2 = <30,8>
Result of p1/p2 = <8,32>
Result of p1+p2*p3 = <37,22>
Result of p1*p2/p3+p1 = <205,112>
'''
