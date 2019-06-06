#Print three different strings

print("Today is Thursday")
print("I am learning about if-else statements")
print ("And... I need to go to the gym")


#Write a program that prints a message if a variable is less than 10,
#and a different message if the variable is greater than or equal to 10

a = 3
if a < 10 :
    print("a is a single digit number")
elif a >= 10:
    print("a is not a single digit number")
    
#Write a program that prints a message if a variable is less than or equal to
# 10, another message if the variable is greater than 10 but less than or equal
# to 25, and another message if the variable is greater than 25

b = 19
if b <= 10:
    print("b is a small number")
elif 10 < b <= 25:
    print("b is in between 10 and 25")
elif b > 25:
    print("b is a big number")

#Create a program that divides two variables and prints the remainder

r = b % a
print(r)

#Create a program that takes two variables, divdes them, and print the quotient

q = b // a
print(q)

#Write a program with a variable age assigned to an interger that prints
#different strings depending on what interger age is

age = 20
if age <= 10:
    print("You're so young")
elif age == 20:
    print("You're the same age as me")
elif age >= 30:
    print("You're older than me")
