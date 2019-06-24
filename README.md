# Python
My journey in learning Python guided by "The Self Taught Programmer" by Cory Althoff

# Python Syntax Cheat Sheet 

Python Utilizes proper spacing to distinguish blocks of code 

Python uses a tab or 4 spaces to contain code in a code block. This example below prints "Hello, World" 100 times:
    
    for i in range(100):
      print("Hello, World")
      
To write a comment use the pound/hashtag symbol:
    
    #This is a comment. 
  
To **print** use the keyword *print*():
    
    print("Hello World")
  
## DATA TYPES 
* string - str
* integer - int 
* floating-point number - float
* booleans - bool
* NonType - where None is the value 

Python does not require your to type when making variable declarations. 

    x = 100
    print(x)
    
 >>100
 
 Here x is assigned the value of 100
 
 #### Increment 
    
    x = 10
    x = x + 1 
    print(x)
    
 >>11
OR 

    x = 10
    x += 1
    print(x)
 >>11
 
## Arithmetic Iperators 
* ** ~ Exponent 
* % ~ Modulo
* // ~ Integer Division/Flooored Quotient
* / ~ Division
* '*' ~ Multiplication 
* '-' ~ Subtraction
* '+' ~ Addition

## Comparison Operators
* '>' ~ Greater Than 
* '<' ~ Less Than
* '>=' ~ Greater Than or Equal To
* '<=' ~ Less Than or Equal To
* '==' ~ Equal 
* '!=' ~ Not Equal 

## Logical Operators 
 * and = and ( True and True = True)
 * or = or (True or False = True)
 * not  = no (not True = False)
 
## Conditional statements 
  * if-statement
        
        home = "America
        if home == "America": 
            print("Hello, America")
  * else-statement
        
        else: 
            print("Hello, World")
  * if-else statement 
  
        home = "America
        if home == "America": 
            print("Hello, America")
        else: 
            print("Hello, World")
            
   * elif-statement
   
            home = "Nigeria"
            if home == "Japan":
                print("Hello, Japan")
            elif home == "Thailand"
                print("Hello, Thailand")
                
## Functions 
Use the key word *def* to define your function and then give your function a name along with parameters to pass in parenthesis

    def functionName(x)
        return x
    
    functionName(3)
    >>3
## Built-In Functions 

* len() - returns the length of the object 
* str() - returns the object as a string 
* int() - returns the object as an integer
* float() - returns the object as a float
* input() - gets input from the user

## Required and Optional Parameters
Python allows you set required parameters and optional parameters 
Required parameters are fufilled when the function is called 
Optional parameters require a default value and do not have to be called with the function

## Variable Scope
**Global Variable** - a variable with global scope that can be read or written to from anywhere in your program 
**Local Variable** - a variable with local scope that can only be read or written to from within the function or class that it is in 

Use the keywokd *global* when writing to a global variable from within a function 
## Error Handeling 
        
        y = input("Give a vauue for y: ")
        
        try: 
            x = int(y)
        except ValueError: 
            print("y must be a number")
        
        >>Give a value for y: 
        
        >>Python
        
        >>y must be a number 
Python Exceptions 
* SyntaxError: EOL while scanning string literal
* ZeroDivisionError: Divison by zero
* IndentationError: Unexpected indent
* ValueError: invalid literal for int() with base 10: 'exampleString'

## Containers

## Lists 
* a container that stopres objects in a specific orfer
* iterable 
* mutable

        list = []
        list = list()
Use index such as "list[1]" to find object in the list at a specific index 
Use *append()* to add to a list 
Use *pop()* to remove last item from list 
Add 2 lists with the addition operator 
Use keyword *in* to check if an item is in a list 
Use keyword *not* paired with *in* to check it an irem is not in a list 

### Tuples 
* a container that stores objects in a specific order 
* mutable 
* iterable 

        
        tuple = ()
        tuple = tuple()
        
 Use index such as tuple[1]
 
 ## Strings 
 
 * strings are immutable 
 * use an index to look up a character, indexed start at 0
 * a **negative index** can be used to look up idems from right to left where [-1] gives the last character in the string 
        
        string = "Hello"
        string[0] = H
        string[-1] = o
* triple quotes can be used to surrpind a string 
        
        string  = """ Line 1 
                      Line 2
                      Line 3
                  """

* use '+' to a strings together 
        
        "string1" + "string2" 
  
  >> "string1string2"
  
* use the asterisk to multiply strings 

        "string1" * 2
        
  >> "string1string1
  
#### Built-In Functions for Strings 

**.upper()** - turns sting to all upper case characters 
**.lower()** - turns string to all lower case characters 
**.captialize()** . - capitalizes the first letter of a string
**.format()** - will indet into the string to replacre the empty {}

**.split()** - splits a string into a list at each x
        
        "blue, pink, purple".split(", ")
**.join()** - used to add new characters between characters of a string 
**.strip()** = strips string of excess white space 
**.replace(x, y)** - when passed two arguments x & y will replace x with y 
**.index()** - returns the index of the first occurence of x in a string 

* use the keyword *in* to check if a string contains another string 
* escape stings within strings by using the backlash 
* \n in a string created a new line 
*use the syntax string[x:y] to slice a string from index x up to index y

-slicing can be used on lists as well 
