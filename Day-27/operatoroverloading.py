'''Operator overloading is the process of giving a special meaning to an operator when it is used with objects of a class.

Example: + → __add__(), > → __gt__()'''
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value
    def __mod__(self,other):
        return self.value%other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __floordiv__(self, other):
        return self.value // other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value
    def __pow__(self,other):
        return self.value**other.value

    def __ne__(self, other):
        return self.value != other.value
    #print(a,b)-convert string to integer and print numbers not like this
    #<__main__.Number object at 0x00000296B9F28590> <__main__.Number object at 0x00000296B9F18690>
    def __str__(self):
        return str(self.value)
a = Number(10)
b = Number(3)
print(a,b)
print(a + b)    
print(a - b)    
print(a * b)    
print(a / b)    
print(a // b)   
print(a > b)    
print(a < b) 
print(a >= b)   
print(a <= b)   
print(a == b)  
print(a != b) 
print(a**b) 
print(a%b)