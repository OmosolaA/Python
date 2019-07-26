# Create Rectangle and Square classes with a method called calculate_perimeter
# that calulates the perimeter of the shapes they represent. Create Rectangle
# and Square objects and call the method on both of them

class Shape:
    #def __init__(self):
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2) 
        

class Square(Shape):
    square_list = []
    
    def __init__(self, s):
        self.side = s
        self.square_list.append(self)
        
    def calculate_perimeter(self):
        return (self.side * 4)

    def change_size(self, number):
        self.side = self.side + number
        return self.side
        
rectangle1 = Rectangle(9, 3)

square1 = Square(5)

print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())

# 2.Define a method in your SQUARE class called change_size that allows you to
# pass in a number that increases or decreases(if the number is negative) each
# side of a SQUARE object by that number.

userNum = input("Please enter a number: ")
userN = int(userNum)
new_square = square1.change_size(userN)
print(new_square)

# 3. Create a class called SHAPE. Define a method in it called what_am_i that
# prints "I am a shape" when called. Change your SQUARE and RECTANGLE classes
# from the previous challenges to inherit from SHAPE, create SQUARE and RECTANGLE
# objects, and call the new method on both of them.

square_shape = Square(7)
rectangle_shape = Rectangle(10, 21)

square_shape.what_am_i()
rectangle_shape.what_am_i()


# 4. Create a class called HORSE and a class called RIDER. Use composition
# to model a horse that has a ride

class Horse:
    def __init__(self, rider):
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

megan = Rider("Megan thee Stallion")
texas = Horse(megan)

print(texas.rider.name)

# Chapter 14: More Object-Oriented Programming
# 1. ADd a square_list class variable to a class called Square so that every time
# you create a new Square object, the new object gets added to the list

#2.Change the Square class so that when you pringt a Square


#3. Write a function that takes two objects as parameters and returns true if they
#are the same object and false if not.

def compareShapes(object1, object2):
    print(object1 is object2)
    
compareShapes(square1, rectangle1)
