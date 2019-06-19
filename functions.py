#Write a function the takes a number as an input and returns that number squared
"""
Gets input from the user
converts the input into an integer
then squares the integer 
"""
x = input("Please enter a number: ")
x = int(x)
def squared():
    y = x * x
    return y


result = squared()
print(result)


#Create a funtion that accepts a string as a parameter and two optional parameters.
"""
Gets input string from the user
then returns the string 
"""

y = input("Please enter a string: ")

def printString():
    return y

string = printString()
print(string)

#Write a function that takes three required parameters and two optional parameters.
"""
uses a, b, and c as required parameters
used d and e as optional parameters
executes simple order of operations problem 
"""

def orderOfOperations(a, b, c, d = 2, e = 3):
    a = int(a)
    b = int(b)
    c = int(c)
    return a + b * c / d + e
 
result = orderOfOperations(10, 20, 30)
print(result)

#Write a program with two functions. The first function should take an integer
#as a parameter and return the result of the integer divided by 2. The second
#function should take an integer as a parameter and return the result of the
#interger multiplied by 4. Call the first function, save the result as a
#variable, and pass it as a parameter to the second function.

"""
uses two functions and uses the result of the first function to execute
the result for the second function
"""

def first(z = 10):
    return z / 2

y = first()
print(y)

def second(y):
    return y * 4

x = second(y)
print(x)

#Write a function that converts a string to a float and returns the result. Use
#exception handling to catch the exception that could occur

"""
converts a string to a float and then uses exception handling 
"""

def floating():
    a = input("Please enter a number: ")
    a = float(a)
    try:
        print(a / 1)
    except ZeroDivisionError:
        print("a cannot be zero.")
    return a

workingFloat = floating()
print(workingFloat)

#Add a docstring to all of the functions you wrote in challenges 1-5
"""
Look at docstrings above 
"""
    
