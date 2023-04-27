#Name: Loc Nguyen
#Date: 04/24/2023
#BOejctive: Conver cpp code to python

#from multipledispatch import dispatch

class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
    #overload + operator and return an object fraction after adding 
    def __add__(self,other):
        return Fraction(self.num*other.den + self.den*other.num,self.den*other.den)
    #overload * operator
    def __mul__(self,other):
        return Fraction(self.num*other.num,self.den*other.den)
    #overload == operator
    def __eq__(self, other):
        return self.num*other.den == self.den*other.num
    #string constructor
    def __str__(self) -> str:
        return (str(self.num)+"/"+str(self.den))
#driver code
def main():
    f1 = Fraction(3,7)
    f2 = Fraction(2,5)
    f3 = Fraction(1,3)
    f4 = Fraction(2,6)
    result = f1 + f2 * f3
    print(result)
    #compare f1 and f3
    if(f1 == f3):
        print("f1 and f3 are the same")
    else:
        print("f1 and f3 are not equal")
    #compare f3 and f4
    if(f3 == f4):
        print("f3 and f4 are the same")
    else: 
        print("f3 and f4 are not equal")
    return 0
#execute driver code
main()
'''Output:
59/105
f1 and f3 are not equal
f3 and f4 are the same'''