# Chapter 22
# FizzBuzz
# Print numbers 1 to 100. For every number that is divisible by 3 print Fizz.
# For every number that is divisible by 5 print Buzz. If a number is divisible
# by both 3 and 5 print FizzBuzz.
# Example:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    
    if (i) % 3 == 0:
        print('Fizz')
        continue

    if (i) % 5 == 0:
        print('Buzz')
        continue
    print(i)
#Twist:
# Print numbers 1 to 100. Given the dictionary below, print the corresponding value
# for each number that is divisible by the key in the dictionary.
#dictionary = {3:'Chocolate', 4:'Cookies n cream', 5:'Red Velvet', 10:'Pazookie'}
print("   ")
print("   ") 
for i in range(1,101):

    if i % 3 == 0:
        print("Chocolate")
        continue
    if i % 4 == 0:
        print("Cookies n Cream")
        continue
    if i % 5 == 0:
        print("Red Velvet")
        continue
    if i % 10 == 0 :
        print("Pazookie")
        continue
    print(i)


#5. Character Count
#Write a function that takes in a word and returns the count of each character in the word.
#Example: The word cookie has 1 c, 2 o's, 1 k, 1 i, 1 e.
