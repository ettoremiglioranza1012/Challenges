import math 
import unittest

class ComplexNumber:
    def __init__(self, real, imaginary):
        # creating an instance for the class 'ComplexNumber'
        self.real = real
        self.imaginary = imaginary
    
    def phase(self):
        # method to return the phase of the complex number
        return math.atan2(self.imaginary, self.real)
    
    def log(self, base):
        # method that returns another complex number, the phase of the complex number 
        return ComplexNumber(math.log(self.real) / math.log(base), self.phase() / math.log(base))
    
    def __str__(self):
        # special method to print the instance
        return str(self.real) + " + " + str(self.imaginary) + " * (i)"
    
    def magnitude(self):
        # method to calculate the magnitude of a prime number 
        return math.sqrt((self.real ** 2) + (self.imaginary ** 2))
    
    def __eq__(self, other):
        # special method to evalute class.self
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary 
        else:
            return NotImplemented 
        
    def isclose(self, other, delta):
        # method to check that the proximity between two vectors 
        sq_dif_1 = ((self.real - other.real) ** 2)
        sq_dif_2 = ((self.imaginary - other.imaginary) ** 2)
        if isinstance(other, ComplexNumber):
            return math.sqrt(sq_dif_1 + sq_dif_2) < delta
        return False
    
    def __add__(self, other):
        # method to implement sum of imaginary numbers 
        if isinstance(other, ComplexNumber):
            return  ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        elif type(other) is int or type(other) is float: 
            return ComplexNumber(self.real + other, self.imaginary)
        else: 
            return NotImplemented 

    def __Radd__(self, other): 
        # reverse add for '5 + ComplexNumber(3,4)'
        if (type(other)) is int or type(other) is float:
            return ComplexNumber(self.real + other, self.imaginary)
        return NotImplemented

    def __mul__(self, other):
        # method to multiplicate imaginary numbers 
        if isinstance(other, ComplexNumber):
            real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
            imag_part = (self.real * other.imaginary) + (self.imaginary * other.real)
            return ComplexNumber(real_part, imag_part)  
        elif type(other) is int or type(other) is float:
            return ComplexNumber(self.real * other, self.imaginary * other)
        else:
            return NotImplemented  
    def __Rmul__(self, other):
        # reverse multiplication
        if type(other) is int or type(other) is float:
            return ComplexNumber(self.real * other, self.imaginary * other)
        return NotImplemented

def main():
    # costant 
    c = ComplexNumber(3.0, 5.0)
    c1 = ComplexNumber(2.0, 4.0)
    delta = 1
    
    # commands 
    #print(c.real)
    #print(c.imaginary)
    #print(c.phase())
    #print(c.log(math.e))
    #print('Complex number is: %s' % c.log(math.e).__str__())
    #print(c.magnitude())
    #print(type(c.__eq__(c1)))
    #print(c.isclose(c1, delta))
    #print(c.__add__(c1).__str__())
    print(c.__mul__(c1).__str__())
    
    

if __name__ == '__main__':
    main()
    

    
    