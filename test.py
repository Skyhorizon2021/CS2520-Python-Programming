import cmath
class Complex:
  def __init__(self, real, imaginary):
    self._real = real
    self._imaginary = imaginary

  def __add__(self,rhsValue):
    real = self._real + rhsValue._real
    imaginary = self._imaginary + rhsValue._imaginary
    return Complex(real, imaginary)
  
sum = Complex(2,4j)
print()