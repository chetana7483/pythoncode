
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a//b



#imethod ! importing specific function
from calculator import substract

#print(add( 5 ,7))

print(substract(7,3))


#importing all the functions of that file
from calculator import *

print(add(5,6))
print(substract(9,3))
print(multiply(3,8))
print(divide(60,10))

#impoting all the functions of that file and import more than one modules
import calculator

print(calculator.add(7,8))
print(calculator.substract(9,7))
print(calculator.multiply(5,8))
print(calculator.divide(45,5))
